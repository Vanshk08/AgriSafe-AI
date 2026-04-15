# AgriSafe AI - API Documentation

## Base URL
```
http://localhost:5000
```

## Authentication
No authentication required for development version.

## Response Format
All responses are in JSON format.

---

## Endpoints

### 1. Health Check

**Endpoint**: `GET /health`

**Description**: Check API server status and model availability

**Response**:
```json
{
  "status": "healthy",
  "timestamp": "2024-04-14T10:30:00.123456",
  "models_loaded": true
}
```

**Status Codes**:
- `200`: Server is healthy and ready

---

### 2. Image Prediction

**Endpoint**: `POST /predict-image`

**Description**: Predict food freshness from an uploaded image

**Content-Type**: `multipart/form-data`

**Request**:
```
Form Data:
- image: <file> (PNG, JPG, JPEG, GIF)
```

**Success Response** (200):
```json
{
  "success": true,
  "prediction": "fresh",
  "confidence": 0.95,
  "confidence_percentage": 95.0,
  "message": "Food classified as fresh with 95.00% confidence"
}
```

**Error Response** (400):
```json
{
  "error": "No image file provided"
}
```

**Error Response** (500):
```json
{
  "error": "Model not loaded. Please train the model first."
}
```

**Status Codes**:
- `200`: Prediction successful
- `400`: Bad request (missing file, invalid format)
- `503`: Service unavailable (model not loaded)
- `500`: Server error

**Notes**:
- File size limit: 5MB
- Supported formats: PNG, JPG, JPEG, GIF
- Image automatically resized to 224×224
- Returns confidence score (0-1) and percentage (0-100)

---

### 3. Risk Prediction

**Endpoint**: `POST /predict-risk`

**Description**: Predict contamination risk based on food properties

**Content-Type**: `application/json`

**Request**:
```json
{
  "food_type": "dairy",
  "storage_time_hours": 24,
  "temperature": 5
}
```

**Parameters**:
| Parameter | Type | Range | Description |
|-----------|------|-------|-------------|
| food_type | string | dairy, meat, seafood, produce, other | Type of food |
| storage_time_hours | number | 0-240 | Hours food has been stored |
| temperature | number | -20 to 50 | Storage temperature in Celsius |

**Success Response** (200):
```json
{
  "success": true,
  "risk_percentage": 25.5,
  "risk_level": "low",
  "safe_to_eat": true,
  "food_type": "dairy",
  "storage_time_hours": 24,
  "temperature": 5,
  "message": "Risk: 25.50% - LOW"
}
```

**Error Response** (400):
```json
{
  "error": "Missing fields: [food_type, storage_time_hours]"
}
```

**Error Response** (400):
```json
{
  "error": "Invalid food type. Valid options: ['dairy', 'meat', 'seafood', 'produce', 'other']"
}
```

**Status Codes**:
- `200`: Prediction successful
- `400`: Bad request (invalid format, missing fields, out of range)
- `503`: Service unavailable (model not loaded)
- `500`: Server error

**Risk Levels**:
- **Low** (0-30%): Safe to consume
- **Medium** (31-70%): Consume with caution
- **High** (71-100%): Not recommended for consumption

**Notes**:
- Risk level automatically determined based on percentage
- safe_to_eat is false for medium and high risk
- Temperature should account for storage method (fridge: ~4°C, freezer: ~-18°C)

---

### 4. Get Food Types

**Endpoint**: `GET /food-types`

**Description**: Get list of available food type options

**Response** (200):
```json
{
  "food_types": [
    "dairy",
    "meat",
    "seafood",
    "produce",
    "other"
  ]
}
```

**Status Codes**:
- `200`: Successfully retrieved food types

---

## Error Responses

### General Error Format

```json
{
  "error": "Error description"
}
```

### Common Error Codes

| Code | Description |
|------|-------------|
| 400 | Bad Request - Invalid input or missing required fields |
| 404 | Not Found - Endpoint does not exist |
| 500 | Internal Server Error - Server-side error |
| 503 | Service Unavailable - Model not loaded |

---

## Example Requests

### Using curl

#### Image Prediction
```bash
curl -X POST \
  -F "image=@/path/to/food.jpg" \
  http://localhost:5000/predict-image
```

#### Risk Prediction
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "food_type": "dairy",
    "storage_time_hours": 24,
    "temperature": 5
  }' \
  http://localhost:5000/predict-risk
```

#### Health Check
```bash
curl http://localhost:5000/health
```

#### Get Food Types
```bash
curl http://localhost:5000/food-types
```

### Using Python requests

```python
import requests

# Image prediction
files = {'image': open('food.jpg', 'rb')}
response = requests.post('http://localhost:5000/predict-image', files=files)
print(response.json())

# Risk prediction
data = {
    'food_type': 'dairy',
    'storage_time_hours': 24,
    'temperature': 5
}
response = requests.post('http://localhost:5000/predict-risk', json=data)
print(response.json())
```

### Using JavaScript fetch

```javascript
// Image prediction
const formData = new FormData();
formData.append('image', fileInput.files[0]);

fetch('http://localhost:5000/predict-image', {
  method: 'POST',
  body: formData
})
.then(res => res.json())
.then(data => console.log(data));

// Risk prediction
fetch('http://localhost:5000/predict-risk', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    food_type: 'dairy',
    storage_time_hours: 24,
    temperature: 5
  })
})
.then(res => res.json())
.then(data => console.log(data));
```

---

## Rate Limiting

No rate limiting is implemented in the development version.

## CORS

CORS is enabled for localhost development. Frontend can communicate with backend without restrictions.

## File Upload Limits

- Maximum file size: 5 MB
- Supported formats: PNG, JPG, JPEG, GIF

## Model Requirements

Both models must be trained before API can make predictions:
- `models/saved_models/food_classifier.h5` - Image classifier
- `models/saved_models/risk_predictor.pkl` - Risk predictor

If models are missing, endpoints will return 503 Service Unavailable.

---

## Changelog

### Version 1.0.0 (2024-04-14)
- Initial release
- Image classification endpoint
- Risk prediction endpoint
- Health check endpoint
- Food types endpoint

---

## Support

For issues or questions about the API:
1. Check this documentation
2. Review error messages carefully
3. Ensure models are trained and loaded
4. Check server logs for detailed error information
