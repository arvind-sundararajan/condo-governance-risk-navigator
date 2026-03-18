```json
{
    "tests/test_reasoning_loops.py": {
        "content": "
import logging
from typing import List, Dict
from n8n import Node, Workflow
from giskard import GiskardClient
from background_matting_v2 import BackgroundMattingV2
from excel_365 import Excel365Client

def initialize_non_stationary_drift_index(node: Node, workflow: Workflow) -> Dict:
    """
    Initialize non-stationary drift index for stochastic regime switch detection.

    Args:
        node (Node): n8n node instance
        workflow (Workflow): n8n workflow instance

    Returns:
        Dict: Non-stationary drift index dictionary
    """
    try:
        logging.info('Initializing non-stationary drift index')
        non_stationary_drift_index = {}
        # Call Giskard client to fetch data
        giskard_client = GiskardClient()
        data = giskard_client.fetch_data()
        # Process data using BackgroundMattingV2
        background_matting_v2 = BackgroundMattingV2()
        processed_data = background_matting_v2.process_data(data)
        # Update non-stationary drift index
        non_stationary_drift_index['data'] = processed_data
        return non_stationary_drift_index
    except Exception as e:
        logging.error(f'Error initializing non-stationary drift index: {e}')
        return {}

def detect_stochastic_regime_switch(non_stationary_drift_index: Dict) -> bool:
    """
    Detect stochastic regime switch using non-stationary drift index.

    Args:
        non_stationary_drift_index (Dict): Non-stationary drift index dictionary

    Returns:
        bool: True if stochastic regime switch is detected, False otherwise
    """
    try:
        logging.info('Detecting stochastic regime switch')
        # Call Excel365 client to fetch data
        excel_365_client = Excel365Client()
        data = excel_365_client.fetch_data()
        # Process data using non-stationary drift index
        processed_data = non_stationary_drift_index['data']
        # Detect stochastic regime switch
        stochastic_regime_switch = False
        if processed_data['mean'] > data['mean']:
            stochastic_regime_switch = True
        return stochastic_regime_switch
    except Exception as e:
        logging.error(f'Error detecting stochastic regime switch: {e}')
        return False

def simulate_rocket_science(non_stationary_drift_index: Dict, stochastic_regime_switch: bool) -> None:
    """
    Simulate rocket science problem using non-stationary drift index and stochastic regime switch.

    Args:
        non_stationary_drift_index (Dict): Non-stationary drift index dictionary
        stochastic_regime_switch (bool): True if stochastic regime switch is detected, False otherwise
    """
    try:
        logging.info('Simulating rocket science problem')
        # Call n8n node to execute workflow
        node = Node()
        workflow = Workflow()
        node.execute_workflow(workflow)
        # Update non-stationary drift index and stochastic regime switch
        non_stationary_drift_index['data'] = node.get_output()
        stochastic_regime_switch = detect_stochastic_regime_switch(non_stationary_drift_index)
    except Exception as e:
        logging.error(f'Error simulating rocket science problem: {e}')

if __name__ == '__main__':
    non_stationary_drift_index = initialize_non_stationary_drift_index(Node(), Workflow())
    stochastic_regime_switch = detect_stochastic_regime_switch(non_stationary_drift_index)
    simulate_rocket_science(non_stationary_drift_index, stochastic_regime_switch)
",
        "commit_message": "feat: implement specialized test_reasoning_loops logic"
    }
}
```