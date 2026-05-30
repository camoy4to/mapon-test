# Defects Identified During Assessment

## DEF-001

### Title

Report generation allows invalid date ranges

### Severity

Medium

### Priority

Medium

### Area

Reports

### Description

The system allows report generation when the start date is later than the end date.

This violates expected business validation rules and may result in reports being generated for invalid periods.

### Preconditions

* User is authenticated
* Report page is accessible

### Steps to Reproduce

1. Open Create Report page
2. Select any report type
3. Select at least one vehicle
4. Set Date From to a later date than Date To
5. Click Generate Report

### Expected Result

The system should prevent report generation and display a validation message indicating that the start date must be earlier than or equal to the end date.

### Actual Result

The report is successfully generated.

### Automation Coverage

Automated in:


tests/test_report_defects.py


### Notes

The issue was identified during exploratory analysis of the report generation workflow.

# DEF-002

### Title

Driver can be removed without confirmation

### Severity

Medium

### Priority

Low

### Area

Vehicle Management

### Description

A driver assignment can be removed by saving an empty driver name without any confirmation dialog or warning.

This may lead to accidental removal of driver assignments.

### Preconditions

* User is authenticated
* Vehicle has an assigned driver

### Steps to Reproduce

1. Open Vehicle Details page
2. Open Edit Driver dialog
3. Remove driver name
4. Save changes

### Expected Result

The system should either:

* Prevent saving an empty driver assignment, or
* Request explicit confirmation before removing the assigned driver

### Actual Result

The driver assignment is removed immediately without confirmation.

### Automation Coverage

Automated in:

tests/test_vehicle_defects.py


### Notes

The issue represents a workflow safety problem rather than a technical failure.

