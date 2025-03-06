# TDMActivity

## Technical Debt Identified:
1. Hardcoded Values:
   
   • The deduction amounts (SSS, Pag-IBIG, Tax) are hardcoded, which limits flexibility when the policy changes.

   • SSS and tax thresholds are based on static values, which may change over time.

3. No Modularization for User Input:
   • get_valid_deduction_input() and get_valid_salary_input() share similar input validation patterns, leading to code duplication.

3.Limited Error Handling:
  • While errors are caught, the solution lacks deeper validation for edge cases, for instance, the negative salary or deduction inputs.

4. Complexity in calculate_deductions():
   • calculate_deductions() handles both deduction calculation and net salary calculation, which can be split into separate functions for better readability.

## Refactoring Improvements:
1. External Configuration for Deductions:
   • The static values for deductions can be externalized into a configuration file, making it easy to modify them without changing code.

2. Modularize Code for Reusability:
   • Create a helper function for common input validation to reduce code duplication.

3. Separation of Logic:
   • Split the calculation of total deductions and net salary into separate methods. This increases clarity and maintainability.

4. Enhanced Error Handling:
   • Introduce more specific error handling for invalid inputs, like salary being zero or negative, or deductions being unreasonable.

5. Improved Naming:
    • Slight improvements in naming conventions for clarity, such as renaming deduction_type to deduction_category for better readability.

## Challenges & Solutions:
1. Dynamic Thresholds: Suggested using external configurations to handle changing deduction thresholds.
2. Input Validation: Abstracted common validation logic to a helper function.
3. Modularity: Broke down large functions for better readability and reusability.
