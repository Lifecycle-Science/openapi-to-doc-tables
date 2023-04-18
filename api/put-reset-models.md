---
id: put-reset-models
title: "ActionHub | Reset Models"
description: "Use this method to clear out the in-memery versions of the processing data sets including program labels, assets, event_types and the event graph."
---
# Reset Models
<code class='method-name'><span class='put'>PUT</span> /program/reset</code>

Use this method to clear out the in-memery versions of the processing data sets including program labels, assets, event_types and the event graph.

## Request Parameters 

### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

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

