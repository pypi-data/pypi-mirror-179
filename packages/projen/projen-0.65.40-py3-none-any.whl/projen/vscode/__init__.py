import abc
import builtins
import datetime
import enum
import typing

import jsii
import publication
import typing_extensions

from typeguard import check_type

from .._jsii import *

from .. import (
    Component as _Component_2b0ad27f,
    DevEnvironmentDockerImage as _DevEnvironmentDockerImage_4a8d8ffd,
    DevEnvironmentOptions as _DevEnvironmentOptions_b10d89d1,
    IDevEnvironment as _IDevEnvironment_9a084622,
    Project as _Project_57d89203,
    Task as _Task_9fa875b6,
)


@jsii.enum(jsii_type="projen.vscode.Console")
class Console(enum.Enum):
    '''(experimental) Controls where to launch the debug target Source: https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes.

    :stability: experimental
    '''

    INTERNAL_CONSOLE = "INTERNAL_CONSOLE"
    '''
    :stability: experimental
    '''
    INTEGRATED_TERMINAL = "INTEGRATED_TERMINAL"
    '''
    :stability: experimental
    '''
    EXTERNAL_TERMINAL = "EXTERNAL_TERMINAL"
    '''
    :stability: experimental
    '''


@jsii.implements(_IDevEnvironment_9a084622)
class DevContainer(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.vscode.DevContainer",
):
    '''(experimental) A development environment running VSCode in a container;

    used by GitHub
    codespaces.

    :stability: experimental
    '''

    def __init__(
        self,
        project: _Project_57d89203,
        *,
        docker_image: typing.Optional[_DevEnvironmentDockerImage_4a8d8ffd] = None,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tasks: typing.Optional[typing.Sequence[_Task_9fa875b6]] = None,
        vscode_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''
        :param project: -
        :param docker_image: (experimental) A Docker image or Dockerfile for the container.
        :param ports: (experimental) An array of ports that should be exposed from the container.
        :param tasks: (experimental) An array of tasks that should be run when the container starts.
        :param vscode_extensions: (experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                project: _Project_57d89203,
                *,
                docker_image: typing.Optional[_DevEnvironmentDockerImage_4a8d8ffd] = None,
                ports: typing.Optional[typing.Sequence[builtins.str]] = None,
                tasks: typing.Optional[typing.Sequence[_Task_9fa875b6]] = None,
                vscode_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        options = DevContainerOptions(
            docker_image=docker_image,
            ports=ports,
            tasks=tasks,
            vscode_extensions=vscode_extensions,
        )

        jsii.create(self.__class__, self, [project, options])

    @jsii.member(jsii_name="addDockerImage")
    def add_docker_image(self, image: _DevEnvironmentDockerImage_4a8d8ffd) -> None:
        '''(experimental) Add a custom Docker image or Dockerfile for the container.

        :param image: -

        :stability: experimental
        '''
        if __debug__:
            def stub(image: _DevEnvironmentDockerImage_4a8d8ffd) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument image", value=image, expected_type=type_hints["image"])
        return typing.cast(None, jsii.invoke(self, "addDockerImage", [image]))

    @jsii.member(jsii_name="addPorts")
    def add_ports(self, *ports: builtins.str) -> None:
        '''(experimental) Adds ports that should be exposed (forwarded) from the container.

        :param ports: The new ports.

        :stability: experimental
        '''
        if __debug__:
            def stub(*ports: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument ports", value=ports, expected_type=typing.Tuple[type_hints["ports"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addPorts", [*ports]))

    @jsii.member(jsii_name="addTasks")
    def add_tasks(self, *tasks: _Task_9fa875b6) -> None:
        '''(experimental) Adds tasks to run when the container starts.

        Tasks will be run in sequence.

        :param tasks: The new tasks.

        :stability: experimental
        '''
        if __debug__:
            def stub(*tasks: _Task_9fa875b6) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument tasks", value=tasks, expected_type=typing.Tuple[type_hints["tasks"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addTasks", [*tasks]))

    @jsii.member(jsii_name="addVscodeExtensions")
    def add_vscode_extensions(self, *extensions: builtins.str) -> None:
        '''(experimental) Adds a list of VSCode extensions that should be automatically installed in the container.

        :param extensions: The extension IDs.

        :stability: experimental
        '''
        if __debug__:
            def stub(*extensions: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument extensions", value=extensions, expected_type=typing.Tuple[type_hints["extensions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addVscodeExtensions", [*extensions]))

    @builtins.property
    @jsii.member(jsii_name="config")
    def config(self) -> typing.Any:
        '''(experimental) Direct access to the devcontainer configuration (escape hatch).

        :stability: experimental
        '''
        return typing.cast(typing.Any, jsii.get(self, "config"))


@jsii.data_type(
    jsii_type="projen.vscode.DevContainerOptions",
    jsii_struct_bases=[_DevEnvironmentOptions_b10d89d1],
    name_mapping={
        "docker_image": "dockerImage",
        "ports": "ports",
        "tasks": "tasks",
        "vscode_extensions": "vscodeExtensions",
    },
)
class DevContainerOptions(_DevEnvironmentOptions_b10d89d1):
    def __init__(
        self,
        *,
        docker_image: typing.Optional[_DevEnvironmentDockerImage_4a8d8ffd] = None,
        ports: typing.Optional[typing.Sequence[builtins.str]] = None,
        tasks: typing.Optional[typing.Sequence[_Task_9fa875b6]] = None,
        vscode_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
    ) -> None:
        '''(experimental) Constructor options for the DevContainer component.

        The default docker image used for GitHub Codespaces is defined here:

        :param docker_image: (experimental) A Docker image or Dockerfile for the container.
        :param ports: (experimental) An array of ports that should be exposed from the container.
        :param tasks: (experimental) An array of tasks that should be run when the container starts.
        :param vscode_extensions: (experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.

        :see: https://github.com/microsoft/vscode-dev-containers/tree/master/containers/codespaces-linux
        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                docker_image: typing.Optional[_DevEnvironmentDockerImage_4a8d8ffd] = None,
                ports: typing.Optional[typing.Sequence[builtins.str]] = None,
                tasks: typing.Optional[typing.Sequence[_Task_9fa875b6]] = None,
                vscode_extensions: typing.Optional[typing.Sequence[builtins.str]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument docker_image", value=docker_image, expected_type=type_hints["docker_image"])
            check_type(argname="argument ports", value=ports, expected_type=type_hints["ports"])
            check_type(argname="argument tasks", value=tasks, expected_type=type_hints["tasks"])
            check_type(argname="argument vscode_extensions", value=vscode_extensions, expected_type=type_hints["vscode_extensions"])
        self._values: typing.Dict[str, typing.Any] = {}
        if docker_image is not None:
            self._values["docker_image"] = docker_image
        if ports is not None:
            self._values["ports"] = ports
        if tasks is not None:
            self._values["tasks"] = tasks
        if vscode_extensions is not None:
            self._values["vscode_extensions"] = vscode_extensions

    @builtins.property
    def docker_image(self) -> typing.Optional[_DevEnvironmentDockerImage_4a8d8ffd]:
        '''(experimental) A Docker image or Dockerfile for the container.

        :stability: experimental
        '''
        result = self._values.get("docker_image")
        return typing.cast(typing.Optional[_DevEnvironmentDockerImage_4a8d8ffd], result)

    @builtins.property
    def ports(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An array of ports that should be exposed from the container.

        :stability: experimental
        '''
        result = self._values.get("ports")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def tasks(self) -> typing.Optional[typing.List[_Task_9fa875b6]]:
        '''(experimental) An array of tasks that should be run when the container starts.

        :stability: experimental
        '''
        result = self._values.get("tasks")
        return typing.cast(typing.Optional[typing.List[_Task_9fa875b6]], result)

    @builtins.property
    def vscode_extensions(self) -> typing.Optional[typing.List[builtins.str]]:
        '''(experimental) An array of extension IDs that specify the extensions that should be installed inside the container when it is created.

        :stability: experimental
        '''
        result = self._values.get("vscode_extensions")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "DevContainerOptions(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.enum(jsii_type="projen.vscode.InternalConsoleOptions")
class InternalConsoleOptions(enum.Enum):
    '''(experimental) Controls the visibility of the VSCode Debug Console panel during a debugging session Source: https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes.

    :stability: experimental
    '''

    NEVER_OPEN = "NEVER_OPEN"
    '''
    :stability: experimental
    '''
    OPEN_ON_FIRST_SESSION_START = "OPEN_ON_FIRST_SESSION_START"
    '''
    :stability: experimental
    '''
    OPEN_ON_SESSION_START = "OPEN_ON_SESSION_START"
    '''
    :stability: experimental
    '''


@jsii.data_type(
    jsii_type="projen.vscode.Presentation",
    jsii_struct_bases=[],
    name_mapping={"group": "group", "hidden": "hidden", "order": "order"},
)
class Presentation:
    def __init__(
        self,
        *,
        group: builtins.str,
        hidden: builtins.bool,
        order: jsii.Number,
    ) -> None:
        '''(experimental) VSCode launch configuration Presentation interface "using the order, group, and hidden attributes in the presentation object you can sort, group, and hide configurations and compounds in the Debug configuration dropdown and in the Debug quick pick." Source: https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes.

        :param group: 
        :param hidden: 
        :param order: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                group: builtins.str,
                hidden: builtins.bool,
                order: jsii.Number,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument group", value=group, expected_type=type_hints["group"])
            check_type(argname="argument hidden", value=hidden, expected_type=type_hints["hidden"])
            check_type(argname="argument order", value=order, expected_type=type_hints["order"])
        self._values: typing.Dict[str, typing.Any] = {
            "group": group,
            "hidden": hidden,
            "order": order,
        }

    @builtins.property
    def group(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("group")
        assert result is not None, "Required property 'group' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def hidden(self) -> builtins.bool:
        '''
        :stability: experimental
        '''
        result = self._values.get("hidden")
        assert result is not None, "Required property 'hidden' is missing"
        return typing.cast(builtins.bool, result)

    @builtins.property
    def order(self) -> jsii.Number:
        '''
        :stability: experimental
        '''
        result = self._values.get("order")
        assert result is not None, "Required property 'order' is missing"
        return typing.cast(jsii.Number, result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "Presentation(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


@jsii.data_type(
    jsii_type="projen.vscode.ServerReadyAction",
    jsii_struct_bases=[],
    name_mapping={"action": "action", "pattern": "pattern", "uri_format": "uriFormat"},
)
class ServerReadyAction:
    def __init__(
        self,
        *,
        action: builtins.str,
        pattern: typing.Optional[builtins.str] = None,
        uri_format: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) VSCode launch configuration ServerReadyAction interface "if you want to open a URL in a web browser whenever the program under debugging outputs a specific message to the debug console or integrated terminal." Source: https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes.

        :param action: 
        :param pattern: 
        :param uri_format: 

        :stability: experimental
        '''
        if __debug__:
            def stub(
                *,
                action: builtins.str,
                pattern: typing.Optional[builtins.str] = None,
                uri_format: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument action", value=action, expected_type=type_hints["action"])
            check_type(argname="argument pattern", value=pattern, expected_type=type_hints["pattern"])
            check_type(argname="argument uri_format", value=uri_format, expected_type=type_hints["uri_format"])
        self._values: typing.Dict[str, typing.Any] = {
            "action": action,
        }
        if pattern is not None:
            self._values["pattern"] = pattern
        if uri_format is not None:
            self._values["uri_format"] = uri_format

    @builtins.property
    def action(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("action")
        assert result is not None, "Required property 'action' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def pattern(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("pattern")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def uri_format(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("uri_format")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "ServerReadyAction(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VsCode(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.vscode.VsCode",
):
    '''
    :stability: experimental
    '''

    def __init__(self, project: _Project_57d89203) -> None:
        '''
        :param project: -

        :stability: experimental
        '''
        if __debug__:
            def stub(project: _Project_57d89203) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument project", value=project, expected_type=type_hints["project"])
        jsii.create(self.__class__, self, [project])

    @builtins.property
    @jsii.member(jsii_name="extensions")
    def extensions(self) -> "VsCodeRecommendedExtensions":
        '''
        :stability: experimental
        '''
        return typing.cast("VsCodeRecommendedExtensions", jsii.get(self, "extensions"))

    @builtins.property
    @jsii.member(jsii_name="launchConfiguration")
    def launch_configuration(self) -> "VsCodeLaunchConfig":
        '''
        :stability: experimental
        '''
        return typing.cast("VsCodeLaunchConfig", jsii.get(self, "launchConfiguration"))

    @builtins.property
    @jsii.member(jsii_name="settings")
    def settings(self) -> "VsCodeSettings":
        '''
        :stability: experimental
        '''
        return typing.cast("VsCodeSettings", jsii.get(self, "settings"))


class VsCodeLaunchConfig(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.vscode.VsCodeLaunchConfig",
):
    '''(experimental) VSCode launch configuration file (launch.json), useful for enabling in-editor debugger.

    :stability: experimental
    '''

    def __init__(self, vscode: VsCode) -> None:
        '''
        :param vscode: -

        :stability: experimental
        '''
        if __debug__:
            def stub(vscode: VsCode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument vscode", value=vscode, expected_type=type_hints["vscode"])
        jsii.create(self.__class__, self, [vscode])

    @jsii.member(jsii_name="addConfiguration")
    def add_configuration(
        self,
        *,
        name: builtins.str,
        request: builtins.str,
        type: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        console: typing.Optional[Console] = None,
        cwd: typing.Optional[builtins.str] = None,
        debug_server: typing.Optional[jsii.Number] = None,
        disable_optimistic_b_ps: typing.Optional[builtins.bool] = None,
        env: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]] = None,
        env_file: typing.Optional[builtins.str] = None,
        internal_console_options: typing.Optional[InternalConsoleOptions] = None,
        out_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        post_debug_task: typing.Optional[builtins.str] = None,
        pre_launch_task: typing.Optional[builtins.str] = None,
        presentation: typing.Optional[typing.Union[Presentation, typing.Dict[str, typing.Any]]] = None,
        program: typing.Optional[builtins.str] = None,
        runtime_args: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_ready_action: typing.Optional[typing.Union[ServerReadyAction, typing.Dict[str, typing.Any]]] = None,
        skip_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        stop_on_entry: typing.Optional[builtins.bool] = None,
        url: typing.Optional[builtins.str] = None,
        web_root: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Adds a VsCodeLaunchConfigurationEntry (e.g. a node.js debugger) to `.vscode/launch.json. Each configuration entry has following mandatory fields: type, request and name. See https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes for details.

        :param name: 
        :param request: 
        :param type: 
        :param args: 
        :param console: 
        :param cwd: 
        :param debug_server: 
        :param disable_optimistic_b_ps: 
        :param env: (experimental) Set value to ``false`` to unset an existing environment variable.
        :param env_file: 
        :param internal_console_options: 
        :param out_files: 
        :param port: 
        :param post_debug_task: 
        :param pre_launch_task: 
        :param presentation: 
        :param program: 
        :param runtime_args: 
        :param server_ready_action: 
        :param skip_files: 
        :param stop_on_entry: 
        :param url: 
        :param web_root: 

        :stability: experimental
        '''
        cfg = VsCodeLaunchConfigurationEntry(
            name=name,
            request=request,
            type=type,
            args=args,
            console=console,
            cwd=cwd,
            debug_server=debug_server,
            disable_optimistic_b_ps=disable_optimistic_b_ps,
            env=env,
            env_file=env_file,
            internal_console_options=internal_console_options,
            out_files=out_files,
            port=port,
            post_debug_task=post_debug_task,
            pre_launch_task=pre_launch_task,
            presentation=presentation,
            program=program,
            runtime_args=runtime_args,
            server_ready_action=server_ready_action,
            skip_files=skip_files,
            stop_on_entry=stop_on_entry,
            url=url,
            web_root=web_root,
        )

        return typing.cast(None, jsii.invoke(self, "addConfiguration", [cfg]))


@jsii.data_type(
    jsii_type="projen.vscode.VsCodeLaunchConfigurationEntry",
    jsii_struct_bases=[],
    name_mapping={
        "name": "name",
        "request": "request",
        "type": "type",
        "args": "args",
        "console": "console",
        "cwd": "cwd",
        "debug_server": "debugServer",
        "disable_optimistic_b_ps": "disableOptimisticBPs",
        "env": "env",
        "env_file": "envFile",
        "internal_console_options": "internalConsoleOptions",
        "out_files": "outFiles",
        "port": "port",
        "post_debug_task": "postDebugTask",
        "pre_launch_task": "preLaunchTask",
        "presentation": "presentation",
        "program": "program",
        "runtime_args": "runtimeArgs",
        "server_ready_action": "serverReadyAction",
        "skip_files": "skipFiles",
        "stop_on_entry": "stopOnEntry",
        "url": "url",
        "web_root": "webRoot",
    },
)
class VsCodeLaunchConfigurationEntry:
    def __init__(
        self,
        *,
        name: builtins.str,
        request: builtins.str,
        type: builtins.str,
        args: typing.Optional[typing.Sequence[builtins.str]] = None,
        console: typing.Optional[Console] = None,
        cwd: typing.Optional[builtins.str] = None,
        debug_server: typing.Optional[jsii.Number] = None,
        disable_optimistic_b_ps: typing.Optional[builtins.bool] = None,
        env: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]] = None,
        env_file: typing.Optional[builtins.str] = None,
        internal_console_options: typing.Optional[InternalConsoleOptions] = None,
        out_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        port: typing.Optional[jsii.Number] = None,
        post_debug_task: typing.Optional[builtins.str] = None,
        pre_launch_task: typing.Optional[builtins.str] = None,
        presentation: typing.Optional[typing.Union[Presentation, typing.Dict[str, typing.Any]]] = None,
        program: typing.Optional[builtins.str] = None,
        runtime_args: typing.Optional[typing.Sequence[builtins.str]] = None,
        server_ready_action: typing.Optional[typing.Union[ServerReadyAction, typing.Dict[str, typing.Any]]] = None,
        skip_files: typing.Optional[typing.Sequence[builtins.str]] = None,
        stop_on_entry: typing.Optional[builtins.bool] = None,
        url: typing.Optional[builtins.str] = None,
        web_root: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Options for a 'VsCodeLaunchConfigurationEntry' Source: https://code.visualstudio.com/docs/editor/debugging#_launchjson-attributes.

        :param name: 
        :param request: 
        :param type: 
        :param args: 
        :param console: 
        :param cwd: 
        :param debug_server: 
        :param disable_optimistic_b_ps: 
        :param env: (experimental) Set value to ``false`` to unset an existing environment variable.
        :param env_file: 
        :param internal_console_options: 
        :param out_files: 
        :param port: 
        :param post_debug_task: 
        :param pre_launch_task: 
        :param presentation: 
        :param program: 
        :param runtime_args: 
        :param server_ready_action: 
        :param skip_files: 
        :param stop_on_entry: 
        :param url: 
        :param web_root: 

        :stability: experimental
        '''
        if isinstance(presentation, dict):
            presentation = Presentation(**presentation)
        if isinstance(server_ready_action, dict):
            server_ready_action = ServerReadyAction(**server_ready_action)
        if __debug__:
            def stub(
                *,
                name: builtins.str,
                request: builtins.str,
                type: builtins.str,
                args: typing.Optional[typing.Sequence[builtins.str]] = None,
                console: typing.Optional[Console] = None,
                cwd: typing.Optional[builtins.str] = None,
                debug_server: typing.Optional[jsii.Number] = None,
                disable_optimistic_b_ps: typing.Optional[builtins.bool] = None,
                env: typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]] = None,
                env_file: typing.Optional[builtins.str] = None,
                internal_console_options: typing.Optional[InternalConsoleOptions] = None,
                out_files: typing.Optional[typing.Sequence[builtins.str]] = None,
                port: typing.Optional[jsii.Number] = None,
                post_debug_task: typing.Optional[builtins.str] = None,
                pre_launch_task: typing.Optional[builtins.str] = None,
                presentation: typing.Optional[typing.Union[Presentation, typing.Dict[str, typing.Any]]] = None,
                program: typing.Optional[builtins.str] = None,
                runtime_args: typing.Optional[typing.Sequence[builtins.str]] = None,
                server_ready_action: typing.Optional[typing.Union[ServerReadyAction, typing.Dict[str, typing.Any]]] = None,
                skip_files: typing.Optional[typing.Sequence[builtins.str]] = None,
                stop_on_entry: typing.Optional[builtins.bool] = None,
                url: typing.Optional[builtins.str] = None,
                web_root: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument name", value=name, expected_type=type_hints["name"])
            check_type(argname="argument request", value=request, expected_type=type_hints["request"])
            check_type(argname="argument type", value=type, expected_type=type_hints["type"])
            check_type(argname="argument args", value=args, expected_type=type_hints["args"])
            check_type(argname="argument console", value=console, expected_type=type_hints["console"])
            check_type(argname="argument cwd", value=cwd, expected_type=type_hints["cwd"])
            check_type(argname="argument debug_server", value=debug_server, expected_type=type_hints["debug_server"])
            check_type(argname="argument disable_optimistic_b_ps", value=disable_optimistic_b_ps, expected_type=type_hints["disable_optimistic_b_ps"])
            check_type(argname="argument env", value=env, expected_type=type_hints["env"])
            check_type(argname="argument env_file", value=env_file, expected_type=type_hints["env_file"])
            check_type(argname="argument internal_console_options", value=internal_console_options, expected_type=type_hints["internal_console_options"])
            check_type(argname="argument out_files", value=out_files, expected_type=type_hints["out_files"])
            check_type(argname="argument port", value=port, expected_type=type_hints["port"])
            check_type(argname="argument post_debug_task", value=post_debug_task, expected_type=type_hints["post_debug_task"])
            check_type(argname="argument pre_launch_task", value=pre_launch_task, expected_type=type_hints["pre_launch_task"])
            check_type(argname="argument presentation", value=presentation, expected_type=type_hints["presentation"])
            check_type(argname="argument program", value=program, expected_type=type_hints["program"])
            check_type(argname="argument runtime_args", value=runtime_args, expected_type=type_hints["runtime_args"])
            check_type(argname="argument server_ready_action", value=server_ready_action, expected_type=type_hints["server_ready_action"])
            check_type(argname="argument skip_files", value=skip_files, expected_type=type_hints["skip_files"])
            check_type(argname="argument stop_on_entry", value=stop_on_entry, expected_type=type_hints["stop_on_entry"])
            check_type(argname="argument url", value=url, expected_type=type_hints["url"])
            check_type(argname="argument web_root", value=web_root, expected_type=type_hints["web_root"])
        self._values: typing.Dict[str, typing.Any] = {
            "name": name,
            "request": request,
            "type": type,
        }
        if args is not None:
            self._values["args"] = args
        if console is not None:
            self._values["console"] = console
        if cwd is not None:
            self._values["cwd"] = cwd
        if debug_server is not None:
            self._values["debug_server"] = debug_server
        if disable_optimistic_b_ps is not None:
            self._values["disable_optimistic_b_ps"] = disable_optimistic_b_ps
        if env is not None:
            self._values["env"] = env
        if env_file is not None:
            self._values["env_file"] = env_file
        if internal_console_options is not None:
            self._values["internal_console_options"] = internal_console_options
        if out_files is not None:
            self._values["out_files"] = out_files
        if port is not None:
            self._values["port"] = port
        if post_debug_task is not None:
            self._values["post_debug_task"] = post_debug_task
        if pre_launch_task is not None:
            self._values["pre_launch_task"] = pre_launch_task
        if presentation is not None:
            self._values["presentation"] = presentation
        if program is not None:
            self._values["program"] = program
        if runtime_args is not None:
            self._values["runtime_args"] = runtime_args
        if server_ready_action is not None:
            self._values["server_ready_action"] = server_ready_action
        if skip_files is not None:
            self._values["skip_files"] = skip_files
        if stop_on_entry is not None:
            self._values["stop_on_entry"] = stop_on_entry
        if url is not None:
            self._values["url"] = url
        if web_root is not None:
            self._values["web_root"] = web_root

    @builtins.property
    def name(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("name")
        assert result is not None, "Required property 'name' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def request(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("request")
        assert result is not None, "Required property 'request' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def type(self) -> builtins.str:
        '''
        :stability: experimental
        '''
        result = self._values.get("type")
        assert result is not None, "Required property 'type' is missing"
        return typing.cast(builtins.str, result)

    @builtins.property
    def args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def console(self) -> typing.Optional[Console]:
        '''
        :stability: experimental
        '''
        result = self._values.get("console")
        return typing.cast(typing.Optional[Console], result)

    @builtins.property
    def cwd(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("cwd")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def debug_server(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("debug_server")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def disable_optimistic_b_ps(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("disable_optimistic_b_ps")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def env(
        self,
    ) -> typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]]:
        '''(experimental) Set value to ``false`` to unset an existing environment variable.

        :stability: experimental
        '''
        result = self._values.get("env")
        return typing.cast(typing.Optional[typing.Mapping[builtins.str, typing.Union[builtins.str, builtins.bool]]], result)

    @builtins.property
    def env_file(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("env_file")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def internal_console_options(self) -> typing.Optional[InternalConsoleOptions]:
        '''
        :stability: experimental
        '''
        result = self._values.get("internal_console_options")
        return typing.cast(typing.Optional[InternalConsoleOptions], result)

    @builtins.property
    def out_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("out_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def port(self) -> typing.Optional[jsii.Number]:
        '''
        :stability: experimental
        '''
        result = self._values.get("port")
        return typing.cast(typing.Optional[jsii.Number], result)

    @builtins.property
    def post_debug_task(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("post_debug_task")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def pre_launch_task(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("pre_launch_task")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def presentation(self) -> typing.Optional[Presentation]:
        '''
        :stability: experimental
        '''
        result = self._values.get("presentation")
        return typing.cast(typing.Optional[Presentation], result)

    @builtins.property
    def program(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("program")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def runtime_args(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("runtime_args")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def server_ready_action(self) -> typing.Optional[ServerReadyAction]:
        '''
        :stability: experimental
        '''
        result = self._values.get("server_ready_action")
        return typing.cast(typing.Optional[ServerReadyAction], result)

    @builtins.property
    def skip_files(self) -> typing.Optional[typing.List[builtins.str]]:
        '''
        :stability: experimental
        '''
        result = self._values.get("skip_files")
        return typing.cast(typing.Optional[typing.List[builtins.str]], result)

    @builtins.property
    def stop_on_entry(self) -> typing.Optional[builtins.bool]:
        '''
        :stability: experimental
        '''
        result = self._values.get("stop_on_entry")
        return typing.cast(typing.Optional[builtins.bool], result)

    @builtins.property
    def url(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("url")
        return typing.cast(typing.Optional[builtins.str], result)

    @builtins.property
    def web_root(self) -> typing.Optional[builtins.str]:
        '''
        :stability: experimental
        '''
        result = self._values.get("web_root")
        return typing.cast(typing.Optional[builtins.str], result)

    def __eq__(self, rhs: typing.Any) -> builtins.bool:
        return isinstance(rhs, self.__class__) and rhs._values == self._values

    def __ne__(self, rhs: typing.Any) -> builtins.bool:
        return not (rhs == self)

    def __repr__(self) -> str:
        return "VsCodeLaunchConfigurationEntry(%s)" % ", ".join(
            k + "=" + repr(v) for k, v in self._values.items()
        )


class VsCodeRecommendedExtensions(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.vscode.VsCodeRecommendedExtensions",
):
    '''(experimental) VS Code Workspace recommended extensions Source: https://code.visualstudio.com/docs/editor/extension-marketplace#_workspace-recommended-extensions.

    :stability: experimental
    '''

    def __init__(self, vscode: VsCode) -> None:
        '''
        :param vscode: -

        :stability: experimental
        '''
        if __debug__:
            def stub(vscode: VsCode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument vscode", value=vscode, expected_type=type_hints["vscode"])
        jsii.create(self.__class__, self, [vscode])

    @jsii.member(jsii_name="addRecommendations")
    def add_recommendations(self, *extensions: builtins.str) -> None:
        '''(experimental) Adds a list of VS Code extensions as recommendations for this workspace.

        :param extensions: The extension IDs.

        :stability: experimental
        '''
        if __debug__:
            def stub(*extensions: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument extensions", value=extensions, expected_type=typing.Tuple[type_hints["extensions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addRecommendations", [*extensions]))

    @jsii.member(jsii_name="addUnwantedRecommendations")
    def add_unwanted_recommendations(self, *extensions: builtins.str) -> None:
        '''(experimental) Marks a list of VS Code extensions as unwanted recommendations for this workspace.

        VS Code should not be recommend these extensions for users of this workspace.

        :param extensions: The extension IDs.

        :stability: experimental
        '''
        if __debug__:
            def stub(*extensions: builtins.str) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument extensions", value=extensions, expected_type=typing.Tuple[type_hints["extensions"], ...]) # pyright: ignore [reportGeneralTypeIssues]
        return typing.cast(None, jsii.invoke(self, "addUnwantedRecommendations", [*extensions]))


class VsCodeSettings(
    _Component_2b0ad27f,
    metaclass=jsii.JSIIMeta,
    jsii_type="projen.vscode.VsCodeSettings",
):
    '''(experimental) VS Code Workspace settings Source: https://code.visualstudio.com/docs/getstarted/settings#_workspace-settings.

    :stability: experimental
    '''

    def __init__(self, vscode: VsCode) -> None:
        '''
        :param vscode: -

        :stability: experimental
        '''
        if __debug__:
            def stub(vscode: VsCode) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument vscode", value=vscode, expected_type=type_hints["vscode"])
        jsii.create(self.__class__, self, [vscode])

    @jsii.member(jsii_name="addSetting")
    def add_setting(
        self,
        setting: builtins.str,
        value: typing.Any,
        language: typing.Optional[builtins.str] = None,
    ) -> None:
        '''(experimental) Adds a workspace setting.

        :param setting: The setting ID.
        :param value: The value of the setting.
        :param language: Scope the setting to a specific language.

        :stability: experimental
        '''
        if __debug__:
            def stub(
                setting: builtins.str,
                value: typing.Any,
                language: typing.Optional[builtins.str] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument setting", value=setting, expected_type=type_hints["setting"])
            check_type(argname="argument value", value=value, expected_type=type_hints["value"])
            check_type(argname="argument language", value=language, expected_type=type_hints["language"])
        return typing.cast(None, jsii.invoke(self, "addSetting", [setting, value, language]))

    @jsii.member(jsii_name="addSettings")
    def add_settings(
        self,
        settings: typing.Mapping[builtins.str, typing.Any],
        languages: typing.Optional[typing.Union[builtins.str, typing.Sequence[builtins.str]]] = None,
    ) -> None:
        '''(experimental) Adds a workspace setting.

        :param settings: Array structure: [setting: string, value: any, languages?: string[]].
        :param languages: -

        :stability: experimental
        '''
        if __debug__:
            def stub(
                settings: typing.Mapping[builtins.str, typing.Any],
                languages: typing.Optional[typing.Union[builtins.str, typing.Sequence[builtins.str]]] = None,
            ) -> None:
                ...
            type_hints = typing.get_type_hints(stub)
            check_type(argname="argument settings", value=settings, expected_type=type_hints["settings"])
            check_type(argname="argument languages", value=languages, expected_type=type_hints["languages"])
        return typing.cast(None, jsii.invoke(self, "addSettings", [settings, languages]))


__all__ = [
    "Console",
    "DevContainer",
    "DevContainerOptions",
    "InternalConsoleOptions",
    "Presentation",
    "ServerReadyAction",
    "VsCode",
    "VsCodeLaunchConfig",
    "VsCodeLaunchConfigurationEntry",
    "VsCodeRecommendedExtensions",
    "VsCodeSettings",
]

publication.publish()
