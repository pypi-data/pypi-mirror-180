from typing import Sequence, cast, overload

from dlt.common.schema import Schema
from dlt.common.schema.typing import TColumnSchema, TWriteDisposition

from dlt.common.typing import TSecretValue, Any
from dlt.common.configuration import with_config
from dlt.common.configuration.container import Container
from dlt.common.configuration.inject import get_orig_args, last_config
from dlt.common.destination import DestinationReference, TDestinationReferenceArg
from dlt.common.pipeline import LoadInfo, PipelineContext, get_default_working_dir

from dlt.pipeline.configuration import PipelineConfiguration, ensure_correct_pipeline_kwargs
from dlt.pipeline.pipeline import Pipeline


@overload
def pipeline(
    pipeline_name: str = None,
    pipelines_dir: str = None,
    pipeline_salt: TSecretValue = None,
    destination: TDestinationReferenceArg = None,
    dataset_name: str = None,
    import_schema_path: str = None,
    export_schema_path: str = None,
    full_refresh: bool = False,
    credentials: Any = None
) -> Pipeline:
    """Creates a new instance of `dlt` pipeline, which moves the data from the source ie. a REST API and a destination ie. database or a data lake.

    The `pipeline` functions allows you to pass the destination name to which the data should be loaded, the name of the dataset and several other options that govern loading of the data.
    The created `Pipeline` object lets you load the data from any source with `run` method or to have more granular control over the loading process with `extract`, `normalize` and `load` methods.

    Please refer to the following doc pages
    - Write your first pipeline walkthrough: https://dlthub.com/docs/walkthroughs/create-a-pipeline
    - Pipeline architecture and data loading steps: https://dlthub.com/docs/architecture
    - List of supported destinations: https://dlthub.com/docs/destinations

    Args:
        pipeline_name (str, optional): A name of the pipeline that will be used to identify it in monitoring events and to restore its state and data schemas on subsequent runs.
        Defaults to the file name of pipeline script with `dlt_` prefix added.

        pipelines_dir (str, optional): A working directory in which pipeline state and temporary files will be stored. Defaults to user home directory: `~/dlt/pipelines/`.

        pipeline_salt (TSecretValue, optional): A random value used for deterministic hashing during data anonymization. Defaults to a value derived from the pipeline name.
        Default value should not be used for any cryptographic purposes.

        destination (str | DestinationReference, optional): A name of the destination to which dlt will load the data, or a destination module imported from `dlt.destination`.
        May also be provided to `run` method of the `pipeline`.

        dataset_name (str, optional): A name of the dataset to which the data will be loaded. A dataset is a logical group of tables ie. `schema` in relational databases or folder grouping many files.
        May also be provided later to the `run` or `load` methods of the `Pipeline`. If not provided at all then defaults to the `pipeline_name`

        import_schema_path (str, optional): A path from which the schema `yaml` file will be imported on each pipeline run. Defaults to None which disables importing.

        export_schema_path (str, optional): A path where the schema `yaml` file will be exported after every schema change. Defaults to None which disables exporting.

        full_refresh (bool, optional): When set to True, each instance of the pipeline with the `pipeline_name` starts from scratch when run and loads the data to a separate dataset.
        The datasets are identified by `dataset_name_` + datetime suffix. Use this setting whenever you experiment with your data to be sure you start fresh on each run. Defaults to False.

        credentials (Any, optional): Credentials for the `destination` ie. database connection string or a dictionary with google cloud credentials.
        In most cases should be set to None, which lets `dlt` to use `secrets.toml` or environment variables to infer right credentials values.

    Returns:
        Pipeline: An instance of `dlt` pipeline with a `run` method to which you should pass your data.
    """


@overload
def pipeline() -> Pipeline:  # type: ignore
    """When called without any arguments, returns the recently created `Pipeline` instance or creates a new instance with all the pipeline options set to defaults."""


@with_config(spec=PipelineConfiguration, auto_namespace=True)
def pipeline(
    pipeline_name: str = None,
    pipelines_dir: str = None,
    pipeline_salt: TSecretValue = None,
    destination: TDestinationReferenceArg = None,
    dataset_name: str = None,
    import_schema_path: str = None,
    export_schema_path: str = None,
    full_refresh: bool = False,
    credentials: Any = None,
    **kwargs: Any
) -> Pipeline:
    ensure_correct_pipeline_kwargs(pipeline, **kwargs)
    # call without arguments returns current pipeline
    orig_args = get_orig_args(**kwargs)  # original (*args, **kwargs)
    # is any of the arguments different from defaults
    has_arguments = bool(orig_args[0]) or any(orig_args[1].values())

    if not has_arguments:
        context = Container()[PipelineContext]
        # if pipeline instance is already active then return it, otherwise create a new one
        if context.is_active():
            return cast(Pipeline, context.pipeline())
        else:
            pass

    # if working_dir not provided use temp folder
    if not pipelines_dir:
        pipelines_dir = get_default_working_dir()

    destination = DestinationReference.from_name(destination or kwargs["destination_name"])
    # create new pipeline instance
    p = Pipeline(
        pipeline_name,
        pipelines_dir,
        pipeline_salt,
        destination,
        dataset_name,
        credentials,
        import_schema_path,
        export_schema_path,
        full_refresh,
        False,
        last_config(**kwargs),
        kwargs["runtime"])
    # set it as current pipeline
    Container()[PipelineContext].activate(p)

    return p


@with_config(spec=PipelineConfiguration, auto_namespace=True)
def attach(
    pipeline_name: str = None,
    pipelines_dir: str = None,
    pipeline_salt: TSecretValue = None,
    full_refresh: bool = False,
    **kwargs: Any
) -> Pipeline:
    ensure_correct_pipeline_kwargs(attach, **kwargs)
    # if working_dir not provided use temp folder
    if not pipelines_dir:
        pipelines_dir = get_default_working_dir()
    # create new pipeline instance
    p = Pipeline(pipeline_name, pipelines_dir, pipeline_salt, None, None, None, None, None, full_refresh, True, last_config(**kwargs), kwargs["runtime"])
    # set it as current pipeline
    Container()[PipelineContext].activate(p)
    return p


def run(
    data: Any,
    *,
    destination: TDestinationReferenceArg = None,
    dataset_name: str = None,
    credentials: Any = None,
    table_name: str = None,
    write_disposition: TWriteDisposition = None,
    columns: Sequence[TColumnSchema] = None,
    schema: Schema = None
) -> LoadInfo:
    """Loads the data in `data` argument into the `destination`


    Args:
        data (Any): _description_
        destination (TDestinationReferenceArg, optional): _description_. Defaults to None.
        dataset_name (str, optional): _description_. Defaults to None.
        credentials (Any, optional): _description_. Defaults to None.
        table_name (str, optional): _description_. Defaults to None.
        write_disposition (TWriteDisposition, optional): _description_. Defaults to None.
        columns (Sequence[TColumnSchema], optional): _description_. Defaults to None.
        schema (Schema, optional): _description_. Defaults to None.

    Raises:
        PipelineStepFailed
    Returns:
        LoadInfo: _description_
    """
    destination = DestinationReference.from_name(destination)
    return pipeline().run(
        data,
        destination=destination,
        dataset_name=dataset_name,
        credentials=credentials,
        table_name=table_name,
        write_disposition=write_disposition,
        columns=columns,
        schema=schema
    )


# setup default pipeline in the container
Container()[PipelineContext] = PipelineContext(pipeline)
