# Documentation for USAID SCCT Project

This page contains various documentation artifacts supporting the USAID SCCT workstreams.  This includes any confluence/wiki pages, etc.  It will also include any automated scripts, etc. used to create/manage documentation.

## ER Diagrams

Using PlantUML/Mermaid ER diagrams can be created and managed using markdown syntax.  See DataDictionary-3.8.xlsx for details on the ER model for the One Network systems. 
The below diagrams are created using [Mermaid ER Diagram](https://mermaid.js.org/syntax/entityRelationshipDiagram.html "Mermaid ER Diagram") syntax.


```mermaid
erDiagram
    CUSTOMER ||--o{ ORDER : places
    CUSTOMER {
        string name
        string custNumber
        string sector
    }
    ORDER ||--|{ LINE-ITEM : contains
    ORDER {
        int orderNumber
        string deliveryAddress
    }
    LINE-ITEM {
        string productCode
        int quantity
        float pricePerUnit
    }
    ENTERPRISE	{
    string OMS_EXTERNAL_INVOICE_SYSTEM
    int OMS_SYS_VANENTERPRISE_ID
    int SYS_CREATION_TEMPLATE_ID
    int	SYS_HIFI_SCENARIO_ID
    int	SYS_ENT_ID
    string APPT_SCHEDULING_SYSTEM
    }
    ORGANIZATION {
    int OMS_SYS_INVOICEE_MGMT_ORG_ID
    int OMS_SYS_INVOICER_MGMT_ORG_ID
    int OMS_SYS_REQUISTION_MGMT_ORG_ID
    int SYS_CREATION_TEMPLATE_ID
    int SYS_ENT_ID
    int SYS_ORG_ID
}



```

[TOC levels=2]: # "### Table of contents"

