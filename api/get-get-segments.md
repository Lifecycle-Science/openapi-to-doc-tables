---
id: get-get-segments
title: "ActionHub | Get Segments"
description: "Get list of user counts for single asset-based or label-based segments."
---
# Get Segments
<code class='method-name'><span class='get'>GET</span> /segments</code>

Get list of user counts for single asset-based or label-based segments.

## Request Parameters 

### Query Parameters  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Description</th></tr><tr><td><code>segment_type</code></td><td></td><td>

Default: growth<br/>Indicates if the segment should consider all growth values (default), only values matching a user history (base), or only values that are net new for the user (discovery). See product documentation for more details about segment types

</td></tr><tr><td><code>segment_basis</code></td><td></td><td>

Default: labels<br/>Specifies whether the segments should be broken out by asset or label.

</td></tr><tr><td><code>min_weight</code></td><td>number</td><td>

Default: 0.5<br/>Minimum weight allowable for asset and label recommendations to qualify for the segment.

</td></tr><tr><td><code>force_refresh</code></td><td>boolean</td><td>

Default: False<br/>Recalculate the segment counts and do not use the cache

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

Page_SegmentCount_ | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>items</code> <span class='required'>required</span></td><td>array</td><td>

items: {'$ref': '#/components/schemas/SegmentCount'}<br/>
</td></tr><tr><td><code>total</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 0.0<br/>
</td></tr><tr><td><code>page</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 1.0<br/>
</td></tr><tr><td><code>size</code> <span class='required'>required</span></td><td>integer</td><td>

minimum: 1.0<br/>
</td></tr></table>

SegmentCount | `application/json`  
<table class='openapi-table'><tr><th>Name</th><th>Type</th><th>Properties</th></tr><tr><td><code>segment_type</code> <span class='required'>required</span></td><td>string</td><td>

description: Either `growth` (actions to drive overall engagement), `discovery` (actions for exploration), or `base` (actions for repeat behaviors).<br/>
</td></tr><tr><td><code>segment_basis</code> <span class='required'>required</span></td><td>string</td><td>

description: Ether `label` or `asset`<br/>
</td></tr><tr><td><code>segment_basis_id</code> <span class='required'>required</span></td><td>string</td><td>

description: Ether the `label` or `asset` id<br/>
</td></tr><tr><td><code>action_type</code> <span class='required'>required</span></td><td>string</td><td>

description: Recommended event_type<br/>
</td></tr><tr><td><code>name</code> <span class='required'>required</span></td><td>string</td><td>


</td></tr><tr><td><code>user_count</code> <span class='required'>required</span></td><td>integer</td><td>

description: The number of users in the segment<br/>
</td></tr><tr><td><code>strength</code> <span class='required'>required</span></td><td>number</td><td>

description: The average of the user weights in the segment<br/>
</td></tr><tr><td><code>min_weight</code> <span class='required'>required</span></td><td>number</td><td>

description: The cutoff weight for including in the segment<br/>
</td></tr></table>


**Response Example**  

```json
{
  "items": [
    {
      "segment_type": "string",
      "segment_basis": "string",
      "segment_basis_id": "string",
      "action_type": "string",
      "name": "string",
      "user_count": "integer",
      "strength": "number",
      "min_weight": "number"
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

