---
id: put-put-labels
title: "ActionHub | Put Labels"
description: "Upsert function will either add new asset to program, or update existing asset with the same asset_id"
---
# Put Labels
<code class='method-name'><span class='put'>PUT</span> /labels</code>

Upsert function will either add new asset to program, or update existing asset with the same asset_id

## Request Parameters 

### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Request Body  

LabelList | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>labels</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/Label'}<br/>
</td></tr></table>

Label | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>label</code> <span class='required'>required</span></td><td>string</td><td>

maxLength: 64<br/>
</td></tr><tr><td><code>weight</code> <span class='required'>required</span></td><td>number</td><td>

description: The strength of the action recommendation for the given user. Higher values mean stronger recommendation. <br/>
</td></tr></table>


**Request Example**  

```json
{
  "labels": [
    {
      "label": "string",
      "weight": "number"
    }
  ]
}
```

## Responses  

### `200` Successful Response

SuccessMessage | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>result</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>


**Response Example**  

```json
{
  "result": "string"
}
```

### `422` Validation Error

HTTPValidationError | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>detail</code></td><td>array</td><td>

items: {'$ref': '#/components/schemas/ValidationError'}<br/>
</td></tr></table>

ValidationError | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>loc</code> <span class='required'>required</span></td><td>array</td><td>

items: {'anyOf': [{'type': 'string'}, {'type': 'integer'}]}<br/>
</td></tr><tr><td><code>msg</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>type</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr></table>

