# History

## 0.1.14

Updated

* Improved Guide Definition Registration Responses
  * Errors associated with registration will be available in the responses
* Documentation for most Guide types and properties

Added

* Aliases for guide.models modules so they are accessible on top level import
* GuideStepDefinitionBackgroundTask that runs process() function in the background allowing users to navigate away from the page.
  * Will work in conjunction with LivelyUI APIs so that user can be given live feedback on the progress of the process method.
* More step control options:
  * uiState now has `continueToNextStep` and `continueToNextStepWhenAvailable` available
  * we can now set uiState on process response without requiring status property to be set
    * Example:
      ```python
      # Instead of:
      return SwitchGuideStepApiResponse(
          status=SwitchGuideStepStatus(
              uiState=SwitchGuideStepStatusUiState(
                  returnToSummary=True
              )
          )
      )

      # We can set uiState as:
      return SwitchGuideStepApiResponse(
          uiState=SwitchGuideStepStatusUiState(
              returnToSummary=True
          )
      )
      ```

## 0.1.13

Initial Switch Guides Release
