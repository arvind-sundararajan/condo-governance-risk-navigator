```json
{
    "utils/data_loader.py": {
        "content": "
import logging
from typing import Dict, List
import n8n
from n8n import Workflow
from giskard import Giskard
from background_matting_v2 import BackgroundMattingV2
import pandas as pd
from pandas import DataFrame

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_condominium_data(workflow: Workflow, giskard: Giskard, background_matting_v2: BackgroundMattingV2) -> Dict[str, List[Dict[str, str]]]:
    """
    Load condominium data from various sources.

    Args:
    - workflow (Workflow): n8n workflow instance
    - giskard (Giskard): Giskard instance for stochastic regime switch
    - background_matting_v2 (BackgroundMattingV2): BackgroundMattingV2 instance for non-stationary drift index

    Returns:
    - Dict[str, List[Dict[str, str]]]: Loaded condominium data
    """
    try:
        # Load data from Excel using n8n
        excel_data = workflow.execute_node('Get Excel Data')
        logger.info('Loaded Excel data')

        # Apply stochastic regime switch using Giskard
        stochastic_regime_switch = giskard.stochastic_regime_switch(excel_data)
        logger.info('Applied stochastic regime switch')

        # Calculate non-stationary drift index using BackgroundMattingV2
        non_stationary_drift_index = background_matting_v2.calculate_non_stationary_drift_index(stochastic_regime_switch)
        logger.info('Calculated non-stationary drift index')

        # Load data from Microsoft Excel 365 using n8n
        microsoft_excel_data = workflow.execute_node('Get Microsoft Excel 365 Data')
        logger.info('Loaded Microsoft Excel 365 data')

        # Merge loaded data
        loaded_data = {**excel_data, **microsoft_excel_data}
        logger.info('Merged loaded data')

        return loaded_data
    except Exception as e:
        logger.error(f'Error loading condominium data: {e}')
        return {}

def transform_condominium_data(loaded_data: Dict[str, List[Dict[str, str]]]) -> DataFrame:
    """
    Transform loaded condominium data into a pandas DataFrame.

    Args:
    - loaded_data (Dict[str, List[Dict[str, str]]]): Loaded condominium data

    Returns:
    - DataFrame: Transformed condominium data
    """
    try:
        # Transform loaded data into a pandas DataFrame
        transformed_data = pd.DataFrame(loaded_data)
        logger.info('Transformed loaded data')

        return transformed_data
    except Exception as e:
        logger.error(f'Error transforming condominium data: {e}')
        return pd.DataFrame()

def load_and_transform_condominium_data(workflow: Workflow, giskard: Giskard, background_matting_v2: BackgroundMattingV2) -> DataFrame:
    """
    Load and transform condominium data.

    Args:
    - workflow (Workflow): n8n workflow instance
    - giskard (Giskard): Giskard instance for stochastic regime switch
    - background_matting_v2 (BackgroundMattingV2): BackgroundMattingV2 instance for non-stationary drift index

    Returns:
    - DataFrame: Loaded and transformed condominium data
    """
    try:
        # Load condominium data
        loaded_data = load_condominium_data(workflow, giskard, background_matting_v2)
        logger.info('Loaded condominium data')

        # Transform loaded data
        transformed_data = transform_condominium_data(loaded_data)
        logger.info('Transformed condominium data')

        return transformed_data
    except Exception as e:
        logger.error(f'Error loading and transforming condominium data: {e}')
        return pd.DataFrame()

if __name__ == '__main__':
    # Create n8n workflow instance
    workflow = n8n.Workflow()

    # Create Giskard instance
    giskard = Giskard()

    # Create BackgroundMattingV2 instance
    background_matting_v2 = BackgroundMattingV2()

    # Load and transform condominium data
    transformed_data = load_and_transform_condominium_data(workflow, giskard, background_matting_v2)
    logger.info('Loaded and transformed condominium data')

    # Print transformed data
    print(transformed_data)
",
        "commit_message": "feat: implement specialized data_loader logic"
    }
}
```