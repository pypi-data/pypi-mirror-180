from mage_ai.data_preparation.models.constants import BlockType
from mage_ai.data_preparation.variable_manager import get_variable
from mage_ai.data_preparation.models.block.sql.utils.shared import (
    interpolate_input,
    should_cache_data_from_upstream,
)
from mage_ai.io.config import ConfigKey
from typing import Dict


def create_upstream_block_tables(
    loader,
    block,
    cascade_on_drop: bool = False,
    configuration: Dict = None,
    execution_partition: str = None,
    cache_upstream_dbt_models: bool = False,
):
    from mage_ai.data_preparation.models.block.dbt.utils import (
        parse_attributes,
        source_table_name_for_block,
    )
    configuration = configuration if configuration else block.configuration

    for idx, upstream_block in enumerate(block.upstream_blocks):
        if should_cache_data_from_upstream(block, upstream_block, [
            'data_provider',
        ], [
            ConfigKey.POSTGRES_DBNAME,
            ConfigKey.POSTGRES_HOST,
            ConfigKey.POSTGRES_PORT,
        ]):
            if BlockType.DBT == upstream_block.type and not cache_upstream_dbt_models:
                continue

            table_name = upstream_block.table_name

            df = get_variable(
                upstream_block.pipeline.uuid,
                upstream_block.uuid,
                'output_0',
                partition=execution_partition,
            )

            schema_name = configuration.get('data_provider_schema')

            if BlockType.DBT == block.type and BlockType.DBT != upstream_block.type:
                attributes_dict = parse_attributes(block)
                schema_name = attributes_dict['source_name']
                table_name = source_table_name_for_block(upstream_block)

            loader.export(
                df,
                schema_name,
                table_name,
                cascade_on_drop=cascade_on_drop,
                drop_table_on_replace=True,
                if_exists='replace',
                index=False,
                verbose=False,
            )


def interpolate_input_data(block, query):
    return interpolate_input(
        block,
        query,
    )
