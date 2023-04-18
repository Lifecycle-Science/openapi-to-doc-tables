---
id: get-get-assets
title: "ActionHub | Get Assets"
description: "Retrieve the assets used in a given program"
---
# Get Assets
<code class='method-name'><span class='get'>GET</span> /assets</code>

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

Page_Asset_ | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>items</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/Asset'}<br/>
</td></tr><tr><td><code>total</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 0.0<br/>
</td></tr><tr><td><code>page</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 1.0<br/>
</td></tr><tr><td><code>size</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 1.0<br/>
</td></tr></table>

Asset | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>asset_id</code> <span class='required'>required</span></td><td>string</td><td>

maxLength: 64<br/>
</td></tr><tr><td><code>asset_name</code></td><td>string</td><td>

maxLength: 124<br/>
</td></tr><tr><td><code>labels</code></td><td>array</td><td>

items: {}<br/>
</td></tr></table>


**Response Example**  

```json
{
  "items": [
    {
      "asset_id": "string",
      "asset_name": "string",
      "labels": "array"
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

