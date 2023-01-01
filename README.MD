This script can be ran on PythonAnywhere to track any Python courses - just set the CRN and term for whatever you desire, install the needed libraries & create a .env file. An example .env has been provided in the repository as .exampleenv.


LXML does not work on AWS as it uses C. The last workaround I could find on StackOverflow/other sites suggested using Python 3.6 which is not a valid selection on AWS Lambda anymore. You can run this with Windows Scheduler instead.