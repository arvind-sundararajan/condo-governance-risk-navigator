```json
{
    "tests/test_agent.py": {
        "content": "
import logging
from typing import Dict, List
from n8n import Node, Workflow
from giskard import GiskardClient
from background_matting_v2 import BackgroundMattingV2
from excel_365 import Excel365Client

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestAgent:
    def __init__(self, workflow: Workflow):
        """
        Initialize the TestAgent.

        Args:
        - workflow (Workflow): The n8n workflow.
        """
        self.workflow = workflow
        self.giskard_client = GiskardClient()
        self.background_matting_v2 = BackgroundMattingV2()
        self.excel_365_client = Excel365Client()

    def non_stationary_drift_index(self, data: List[float]) -> float:
        """
        Calculate the non-stationary drift index.

        Args:
        - data (List[float]): The input data.

        Returns:
        - float: The non-stationary drift index.
        """
        try:
            # Calculate the non-stationary drift index using Giskard
            index = self.giskard_client.calculate_drift_index(data)
            logger.info(f'Non-stationary drift index: {index}')
            return index
        except Exception as e:
            logger.error(f'Error calculating non-stationary drift index: {e}')
            return None

    def stochastic_regime_switch(self, data: List[float]) -> Dict[str, float]:
        """
        Perform stochastic regime switch.

        Args:
        - data (List[float]): The input data.

        Returns:
        - Dict[str, float]: The regime switch results.
        """
        try:
            # Perform stochastic regime switch using BackgroundMattingV2
            results = self.background_matting_v2.regime_switch(data)
            logger.info(f'Regime switch results: {results}')
            return results
        except Exception as e:
            logger.error(f'Error performing stochastic regime switch: {e}')
            return {}

    def extract_excel_data(self, workbook: str, sheet: str) -> List[List[float]]:
        """
        Extract data from Excel workbook.

        Args:
        - workbook (str): The Excel workbook name.
        - sheet (str): The Excel sheet name.

        Returns:
        - List[List[float]]: The extracted data.
        """
        try:
            # Extract data from Excel workbook using Excel365Client
            data = self.excel_365_client.extract_data(workbook, sheet)
            logger.info(f'Extracted data: {data}')
            return data
        except Exception as e:
            logger.error(f'Error extracting Excel data: {e}')
            return []

def main():
    # Create a new n8n workflow
    workflow = Workflow()

    # Create a new TestAgent
    test_agent = TestAgent(workflow)

    # Simulate the 'Rocket Science' problem
    data = [1.0, 2.0, 3.0, 4.0, 5.0]
    index = test_agent.non_stationary_drift_index(data)
    results = test_agent.stochastic_regime_switch(data)
    extracted_data = test_agent.extract_excel_data('example_workbook', 'example_sheet')

    # Log the results
    logger.info(f'Non-stationary drift index: {index}')
    logger.info(f'Regime switch results: {results}')
    logger.info(f'Extracted data: {extracted_data}')

if __name__ == '__main__':
    main()
",
        "commit_message": "feat: implement specialized test_agent logic"
    }
}
```