```json
{
    "tool_integration/excel_integration.py": {
        "content": "
import logging
from typing import Dict, List
import n8n
from n8n import Node
from giskard import Giskard
from background_matting_v2 import BackgroundMattingV2
from excel_365 import Excel365

def connect_excel_to_n8n(excel_file: str, n8n_node: Node) -> None:
    """
    Connects Excel to n8n.

    Args:
    - excel_file (str): The path to the Excel file.
    - n8n_node (Node): The n8n node to connect to.

    Returns:
    - None
    """
    try:
        logging.info('Connecting Excel to n8n...')
        excel_data = Excel365(excel_file).get_data()
        n8n_node.send(excel_data)
        logging.info('Connected Excel to n8n successfully.')
    except Exception as e:
        logging.error(f'Error connecting Excel to n8n: {e}')

def integrate_flow_with_excel(excel_file: str, n8n_node: Node) -> None:
    """
    Integrates flow with Excel using n8n.

    Args:
    - excel_file (str): The path to the Excel file.
    - n8n_node (Node): The n8n node to integrate with.

    Returns:
    - None
    """
    try:
        logging.info('Integrating flow with Excel...')
        non_stationary_drift_index = Giskard().calculate_non_stationary_drift_index(excel_file)
        stochastic_regime_switch = BackgroundMattingV2().calculate_stochastic_regime_switch(excel_file)
        n8n_node.send({'non_stationary_drift_index': non_stationary_drift_index, 'stochastic_regime_switch': stochastic_regime_switch})
        logging.info('Integrated flow with Excel successfully.')
    except Exception as e:
        logging.error(f'Error integrating flow with Excel: {e}')

def update_system_instructions(n8n_node: Node, instructions: Dict[str, str]) -> None:
    """
    Updates the system instructions for the n8n node.

    Args:
    - n8n_node (Node): The n8n node to update.
    - instructions (Dict[str, str]): The new instructions.

    Returns:
    - None
    """
    try:
        logging.info('Updating system instructions...')
        n8n_node.update_instructions(instructions)
        logging.info('Updated system instructions successfully.')
    except Exception as e:
        logging.error(f'Error updating system instructions: {e}')

def connect_multiple_workbooks(n8n_node: Node, excel_files: List[str]) -> None:
    """
    Connects multiple Excel workbooks to the n8n node.

    Args:
    - n8n_node (Node): The n8n node to connect to.
    - excel_files (List[str]): The list of Excel files to connect.

    Returns:
    - None
    """
    try:
        logging.info('Connecting multiple Excel workbooks...')
        for excel_file in excel_files:
            excel_data = Excel365(excel_file).get_data()
            n8n_node.send(excel_data)
        logging.info('Connected multiple Excel workbooks successfully.')
    except Exception as e:
        logging.error(f'Error connecting multiple Excel workbooks: {e}')

if __name__ == '__main__':
    # Simulation of the 'Rocket Science' problem
    excel_file = 'rocket_science.xlsx'
    n8n_node = n8n.Node('rocket_science_node')
    connect_excel_to_n8n(excel_file, n8n_node)
    integrate_flow_with_excel(excel_file, n8n_node)
    instructions = {'non_stationary_drift_index': 'calculate_non_stationary_drift_index', 'stochastic_regime_switch': 'calculate_stochastic_regime_switch'}
    update_system_instructions(n8n_node, instructions)
    excel_files = ['rocket_science_1.xlsx', 'rocket_science_2.xlsx']
    connect_multiple_workbooks(n8n_node, excel_files)
",
        "commit_message": "feat: implement specialized excel_integration logic"
    }
}
```