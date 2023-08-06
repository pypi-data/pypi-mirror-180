from __future__ import annotations
from typing import List, Optional
from google.protobuf import field_mask_pb2
from continual.python.sdk.artifacts import ArtifactsManager
from continual.python.sdk.datasets import DatasetManager
from continual.python.sdk.environments import ProjectEnvironmentManager
from continual.python.sdk.runs import RunManager
from continual.rpc.management.v1 import management_pb2
from continual.rpc.management.v1 import types
from continual.python.sdk.resource import Resource
from continual.python.sdk.manager import Manager
from continual.python.sdk.iterators import Pager
from continual.python.sdk.models import ModelManager
from continual.python.sdk.events import EventManager


class OrganizationProjectManager:
    """Manages organization projects."""

    manager: ProjectManager
    parent: str = ""
    client: client.Client

    def __init__(self, parent: str, client: client.Client):
        self.parent = parent
        self.client = client
        self.manager = ProjectManager(parent=self.parent, client=self.client)

    def list(self, page_size: Optional[int] = None) -> List[Project]:
        """List project.

        Arguments:
            page_size: Number of elements.

        Returns:
            A list of organization projects.
        """
        return self.manager.list(page_size)

    def list_all(self) -> Pager[Project]:
        """List all projects.

        Returns:
            An iterator of all organization projects.
        """
        return self.manager.list_all()

    def create(
        self,
        display_name: str,
        project_id: Optional[str] = None,
    ) -> Project:
        """Create a new project.

        Creates a new project within organization.  The project ID by
        default is generated from the display name and must be globally
        unique across all organizations.

        Arguments:
            display_name: Display name.
            project_id: Optional project id.

        Returns:
            A new project
        """
        return self.manager.create(
            display_name=display_name,
            organization=self.parent,
            project_id=project_id,
        )


class ProjectManager(Manager):
    """Manages project resources."""

    name_pattern: str = "projects/{project}"

    def get(self, id: str) -> Project:
        """Get project.

        Arguments:
            id: Project name or id.

        Returns
            A project.
        """

        project_id = id.split("@")[0]
        req = management_pb2.GetProjectRequest(name=self.name(project_id))
        resp = self.client._management.GetProject(req)
        project = Project.from_proto(resp, client=self.client)
        if "@" in id:
            environment = self.client.environments.get(id.split("@")[1])
            project._set_environment(environment)
        return project

    def list(
        self, page_size: Optional[int] = None, filters: List[str] = None
    ) -> List[Project]:
        """List projects.

        Arguments:
            page_size: Number of items to return.

        Returns:
            A list of projects.
        """
        req = management_pb2.ListProjectsRequest(
            parent=self.parent, page_size=page_size, filters=filters
        )
        resp = self.client._management.ListProjects(req)
        return [Project.from_proto(x, client=self.client) for x in resp.projects]

    def list_all(self) -> Pager[Project]:
        """List all projects.

        Pages through all projects using an iterator.

        Returns:
            A iterator of all projects.
        """

        def next_page(next_page_token):
            req = management_pb2.ListProjectsRequest(
                parent=self.parent, page_token=next_page_token
            )
            resp = self.client._management.ListProjects(req)
            return (
                [Project.from_proto(x, client=self.client) for x in resp.projects],
                resp.next_page_token,
            )

        return Pager(next_page)

    def create(
        self,
        display_name: str,
        organization: str,
        project_id: Optional[str] = None,
    ) -> Project:
        """Create an project.

        New projects are identified by a unique project id that is
        generated from the display name.  To set a project id explicitly,
        you can pass `project_id`.  However project ids are globally unique across
        all organizations.

        Arguments:
            display_name: Display name.
            organization: Organization resource name.
            project_id: User-defined project id.

        Returns:
            A new project.
        """
        req = management_pb2.CreateProjectRequest(
            project=Project(
                display_name=display_name,
                organization=organization,
            ).to_proto()
        )

        resp = self.client._management.CreateProject(req)
        return Project.from_proto(resp, client=self.client)

    def delete(self, id: str, delete_schema: bool = False) -> None:
        """Delete an project.

        Arguments:
            id: Project name or id.
        """

        req = management_pb2.DeleteProjectRequest(
            name=self.name(id), delete_schema=delete_schema
        )
        self.client._management.DeleteProject(req)

    def update(
        self,
        id: str,
        display_name: Optional[str] = None,
    ) -> Project:
        """Update project.

        Arguments:
            display_name:  Display name.
        Returns:
            Updated project.
        """
        paths = []
        if display_name is not None:
            paths.append("display_name")

        req = management_pb2.UpdateProjectRequest(
            update_mask=field_mask_pb2.FieldMask(paths=paths),
            project=Project(name=self.name(id), display_name=display_name).to_proto(),
        )
        resp = self.client._management.UpdateProject(req)
        return Project.from_proto(resp, client=self.client)


class Project(Resource, types.Project):
    """Project resource."""

    name_pattern: str = "projects/{project}"
    manager: ProjectManager

    runs: RunManager
    """Runs manager."""

    models: ModelManager
    """Model manager."""

    datasets: DatasetManager
    """Datasets manager."""

    events: EventManager
    """Event manager."""

    environments: ProjectEnvironmentManager
    """Environments manager."""

    def _init(self):
        self.manager = ProjectManager(parent=self.parent, client=self.client)
        self.models = ModelManager(parent=self.name, client=self.client)
        self.datasets = DatasetManager(parent=self.name, client=self.client)
        self.runs = RunManager(parent=self.name, client=self.client)
        self.events = EventManager(parent=self.name, client=self.client)
        self.environments = ProjectEnvironmentManager(
            parent=self.name, client=self.client
        )
        self.environment = None

    def _set_environment(self, environment):
        self.environment = environment
        self.models = ModelManager(parent=self.environment.name, client=self.client)
        self.datasets = DatasetManager(parent=self.environment.name, client=self.client)
        self.artifacts = ArtifactsManager(
            parent=self.environment.name, client=self.client
        )
        self.runs = RunManager(parent=self.environment.name, client=self.client)
        self.events = EventManager(parent=self.environment.name, client=self.client)

    def delete(self, delete_schema: bool = False) -> None:
        """Delete project."""
        self.manager.delete(self.name, delete_schema=delete_schema)

    def update(self, display_name: Optional[str] = None) -> Project:
        """Update project.

        Arguments:
            display_name:  Display name.

        Returns:
            Updated project.
        """
        return self.manager.update(self.name, display_name=display_name)
