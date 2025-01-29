



# USAID_Data_Dictionary
<details>

<summary>Expand contents</summary>

[SALES_ORDER](#SALES_ORDER)

[ENTERPRISE](#ENTERPRISE)

[ORGANIZATION](#ORGANIZATION)

[SITE](#SITE)

</details>


## [SALES_ORDER](#sales_order)
**<font color="green">Description:</font>** Small data set of Sales Order for Testing  
**<font color="green">Subject Area:</font>** Transaction: Order Management  
**<font color="green">Environment:</font>** Data Generation  

|Attribute Name|Description|Data Type|Required|
| :--- | :--- | :--- | :--- |
|Action Name|Actions Supported: OMS.CreateFromInteg, OMS.UpdateFromInteg, OMS.CancelFromInteg, OMS.CreateSOInPlannedState, OMS.CreateSOInQuoteState, OMS.ConvertQuoteToSO, OMS.CreateOrUpdateFromInteg, OMS.CompleteSales|STRING|Y|
|Creation Org Enterprise Name|Order Creation Organization, this is either Creation User's Organization or Order Managing Organization.|STRING|Y|
|Creation Org Name|Order Creation Organization, this is either Creation User's Organization or Order Managing Organization.|STRING|Y|
|Owning Org Enterprise Name|Enterprise Name of the Organization that owns the order.|STRING|Y|
|Owning Org Name|Organization Name of the Organization that owns the order.|STRING|Y|
|Buying Org Enterprise Name|Enterprise Name of the Buyer Organization.|STRING|Y|
|Buying Org Name|Organization Name of the Buyer Organization.|STRING|Y|
|Customer Name|Customer Name as defined in the Customer Master.|STRING|Y|
|Ship To Org Enterprise Name|Enterprise Name of the Ship To Organization.|STRING|Y|
|Ship To Org Name|Organization Name of the Ship To Organization.|STRING|Y|
|Order Number|Order number. May be generated or provided by the user via integration.|STRING|Y|
|Ship To Site Enterprise Name|Enterprise Name of the Ship To Site.|STRING|Y|
|Ship To Site Organization Name|Organization Name of the Ship To Site.|STRING|Y|
|Ship To Site Name|Ship To Site Name.|STRING|Y|
|Ship To Address Street 1|Ship To Address|STRING|Y|
|Ship To Address Street 2|Ship To Address|STRING|Y|
|Ship To Address City|Ship To Address|STRING|Y|
|Ship To Address State|Ship To Address|STRING|Y|
|Ship To Address Zip|Ship To Address|STRING|Y|
|Ship To Address Country|Ship To Address|STRING|Y|
|Trans Mode Name|Mode of transport as defined in the Equipment Type master.|STRING_ENUMERATION|Y|
|FOB Code|Freight Terms of Sale (Free On Board) Code|STRING_ENUMERATION|Y|
|FOB Point|Freight Terms of Sale (Free On Board) charge point (origin, destination)|STRING_ENUMERATION|Y|
|Item Name|Item Name as defined in the Item Master. If ExtItemName not set|STRING|Y|
|Line Type|Product or Service. Defaults to Product.|STRING_ENUMERATION|Y|
|Request Quantity|Request quantity|DOUBLE|Y|
|Quantity UOM|Quantity UOM|STRING_ENUMERATION|Y|
|Currency|Currency code (e.g. USD)|STRING|Y|
|Is Spot|Indicates whether this PO is spot (once off) or contract based|BOOLEAN|Y|
|Is Expedite|Indicates there is a request to expedite the order.|BOOLEAN|Y|
|Buying Agent 1 Enterprise Name|Agent of buyer who may act on behalf of the buyer and manage the order.|STRING|Y|
|Buying Agent 1 Name|Agent of buyer who may act on behalf of the buyer and manage the order.|STRING|Y|
|Buying Agent 2 Enterprise Name|Agent of buyer who may act on behalf of the buyer and manage the order.|STRING|Y|
|Buying Agent 2 Name|Agent of buyer who may act on behalf of the buyer and manage the order.|STRING|Y|
|Requisition Number|None|STRING|Y|
|Requisition Requesting Org Enterprise Name|None|STRING|Y|
|Requisition Requesting Org Name|None|STRING|Y|
|Requisition Line Number|None|STRING|Y|
|LineRequisitionNumber|None|STRING|Y|
|RequisitionLineRequestingOrgName|None|STRING|Y|
|RequisitionLineRequestingOrgEnterpriseName|None|STRING|Y|
|Budget Owning Org Enterprise Name|Funding related|STRING|Y|
|Budget Owning Org Name|None|STRING|Y|
|Task Order|Populate with the PSA TASK Order|STRING|Y|
|Fiscal Year Funding|None|STRING|Y|
|Funding Source |None|STRING|Y|
|Funding Source Details|None|STRING|Y|

## [ENTERPRISE](#enterprise)
**<font color="green">Description:</font>** The highest level in the Enterprise/Organization/Site Hierarchy  
**<font color="green">Subject Area:</font>** Enterprise entity  
**<font color="green">Environment:</font>** Data Generation  

|Attribute Name|Description|Data Type|Required|
| :--- | :--- | :--- | :--- |
|ORGANIZATION_ID|Unique ID that identifies and Organization|INT|Y|
|ORGANIZATION_NAME|Organization Name|STRING|Y|
|ORGANIZATION_DESCRIPTION|Organization Description|STRING|Y|
|DATE_CREATED|Date Organization was created|DATETIME|Y|

## [ORGANIZATION](#organization)
**<font color="green">Description:</font>** Level 2 in the Enterprise/Organization/Site Hierarchy  
**<font color="green">Subject Area:</font>** Organization entity  
**<font color="green">Environment:</font>** Data Generation  

|Attribute Name|Description|Data Type|Required|
| :--- | :--- | :--- | :--- |
|ORGANIZATION_ID|Unique ID that identifies and Organization|INT|Y|
|ORGANIZATION_NAME|Organization Name|STRING|Y|
|ORGANIZATION_DESCRIPTION|Organization Description|STRING|Y|
|ENTERPRISE_ID|FK Link to Enterprise|INT|Y|
|ENTERPRISE_DESCRIPTION|FK Link to Enterprise.Description|STRING|Y|
|DATE_CREATED|Date Organization was created|DATETIME|Y|

## [SITE](#site)
**<font color="green">Description:</font>** Level 3 in the Enterprise/Organization/Site Hierarchy  
**<font color="green">Subject Area:</font>** Site entity  
**<font color="green">Environment:</font>** Data Generation  

|Attribute Name|Description|Data Type|Required|
| :--- | :--- | :--- | :--- |
|SITE_ID|Unique ID that identifies and Organization|INT|Y|
|SITE_NAME|Organization Name|STRING|Y|
|SITE_DESCRIPTION|Organization Description|STRING|Y|
|ORGANIZATION_ID|FK Link to Organization|INT|Y|
|DATE_CREATED|Date Organization was created|DATETIME|Y|
