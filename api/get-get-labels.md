---
id: get-get-labels
title: "ActionHub | Get Labels"
description: "Retrieve the assets used in a given program"
---
# Get Labels
<code class='method-name'><span class='get'>GET</span> /labels</code>

Retrieve the assets used in a given program

## Request Parameters 

### Query Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>search</code></td><td>string</td><td>

Term will be searched for in any field

</td></tr><tr><td><code>page</code></td><td>integer</td><td>

Default: 1<br/>

</td></tr><tr><td><code>size</code></td><td>integer</td><td>

Default: 50<br/>

</td></tr></table>


### Header Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>program-id</code> <span class='required'>required</span></td><td>string</td><td>



</td></tr></table>

## Responses  

### `200` Successful Response

Page_Label_ | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>items</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/Label'}<br/>
</td></tr><tr><td><code>total</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 0.0<br/>
</td></tr><tr><td><code>page</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 1.0<br/>
</td></tr><tr><td><code>size</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 1.0<br/>
</td></tr></table>

Label | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>label</code> <span class='required'>required</span></td><td>string</td><td>

maxLength: 64<br/>
</td></tr><tr><td><code>weight</code> <span class='required'>required</span></td><td>number</td><td>

description: The strength of the action recommendation for the given user. Higher values mean stronger recommendation. <br/>
</td></tr></table>


**Response Example**  

```json
{
  "items": [
    {
      "label": "string",
      "weight": "number"
    }
  ],
  "total": "integer",
  "page": "integer",
  "size": "integer"
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

