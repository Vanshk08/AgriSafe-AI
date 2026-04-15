# 📊 AgriSafe AI - Sample Input Data

Complete guide with sample data for testing all features of AgriSafe AI.

---

## 🎨 1. Image Upload Test Data

### Sample Images to Test

You can use any food images to test:

**Fresh Food (Expected Output: Fresh)**
- Apple
- Banana
- Fresh vegetables
- Fresh meat
- Dairy products

**Spoiled Food (Expected Output: Spoiled)**
- Moldy bread
- Brown/dark spots on fruit
- Discolored vegetables
- Rotten food

### Where to Get Test Images

- **Unsplash**: https://unsplash.com (search "fresh food" or "spoiled food")
- **Pexels**: https://pexels.com
- **Pixabay**: https://pixabay.com
- Take your own photos

---

## 🥬 2. Agricultural Input Data

### Sample Agricultural Input #1: Wheat Farm

```json
{
  "batch_id": "BATCH_001_WHEAT",
  "crop_type": "grain",
  "pesticide_used": "Chlorpyrifos",
  "pesticide_quantity": 1.5,
  "days_since_pesticide": 14,
  "fertilizer_used": "NPK 10-26-26",
  "fertilizer_quantity": 50,
  "irrigation_source": "groundwater",
  "farm_location": "Maharashtra, India",
  "days_since_harvest": 5,
  "farm_area": 2.5
}
```

### Sample Agricultural Input #2: Tomato Farm

```json
{
  "batch_id": "BATCH_002_TOMATO",
  "crop_type": "vegetables",
  "pesticide_used": "Imidacloprid",
  "pesticide_quantity": 2.0,
  "days_since_pesticide": 7,
  "fertilizer_used": "Organic compost",
  "fertilizer_quantity": 100,
  "irrigation_source": "canal",
  "farm_location": "Karnataka, India",
  "days_since_harvest": 2,
  "farm_area": 1.2
}
```

### Sample Agricultural Input #3: Apple Orchard

```json
{
  "batch_id": "BATCH_003_APPLE",
  "crop_type": "fruits",
  "pesticide_used": "Fungicide - Mancozeb",
  "pesticide_quantity": 3.0,
  "days_since_pesticide": 21,
  "fertilizer_used": "Calcium Nitrate",
  "fertilizer_quantity": 75,
  "irrigation_source": "river",
  "farm_location": "Himachal Pradesh, India",
  "days_since_harvest": 10,
  "farm_area": 5.0
}
```

### Sample Agricultural Input #4: Lettuce Farm

```json
{
  "batch_id": "BATCH_004_LETTUCE",
  "crop_type": "leafy_greens",
  "pesticide_used": "Spinosad",
  "pesticide_quantity": 0.8,
  "days_since_pesticide": 3,
  "fertilizer_used": "Liquid seaweed extract",
  "fertilizer_quantity": 20,
  "irrigation_source": "rain",
  "farm_location": "Punjab, India",
  "days_since_harvest": 1,
  "farm_area": 0.5
}
```

### Sample Agricultural Input #5: Rice Paddy

```json
{
  "batch_id": "BATCH_005_RICE",
  "crop_type": "grain",
  "pesticide_used": "Carbofuran",
  "pesticide_quantity": 1.2,
  "days_since_pesticide": 28,
  "fertilizer_used": "Urea (46-0-0)",
  "fertilizer_quantity": 120,
  "irrigation_source": "pumped",
  "farm_location": "West Bengal, India",
  "days_since_harvest": 8,
  "farm_area": 3.0
}
```

---

## 🌡️ 3. Environmental Data

### Sample Environmental Data #1: High Temperature (High Risk)

```json
{
  "batch_id": "BATCH_001_WHEAT",
  "temperature": 35.5,
  "humidity": 65,
  "rainfall": 5,
  "soil_moisture": 45,
  "light_exposure": 10,
  "wind_speed": 8
}
```

### Sample Environmental Data #2: Moderate Conditions (Low-Medium Risk)

```json
{
  "batch_id": "BATCH_002_TOMATO",
  "temperature": 24.0,
  "humidity": 55,
  "rainfall": 15,
  "soil_moisture": 60,
  "light_exposure": 8,
  "wind_speed": 5
}
```

### Sample Environmental Data #3: Cool, Dry Conditions (Low Risk)

```json
{
  "batch_id": "BATCH_003_APPLE",
  "temperature": 15.0,
  "humidity": 40,
  "rainfall": 0,
  "soil_moisture": 50,
  "light_exposure": 6,
  "wind_speed": 3
}
```

---

## 🍎 4. Food Image Prediction Test Cases

### Test Case 1: Fresh Apple
- **Input**: Fresh apple image
- **Expected Output**: 
  - Prediction: Fresh
  - Confidence: 75-95%
  - Risk Percentage: 10-20%
  - Risk Level: Low

### Test Case 2: Spoiled Banana
- **Input**: Spoiled banana with brown spots
- **Expected Output**:
  - Prediction: Spoiled
  - Confidence: 70-90%
  - Risk Percentage: 75-95%
  - Risk Level: High

### Test Case 3: Fresh Tomato
- **Input**: Fresh red tomato image
- **Expected Output**:
  - Prediction: Fresh
  - Confidence: 80-95%
  - Risk Percentage: 15-25%
  - Risk Level: Low

---

## 📋 5. Risk Assessment Form Test

### Test Input #1: High-Risk Scenario

```
Food Type: Meat
Storage Time: 48 hours
Temperature: 28°C (Warm storage)
Humidity: 75%
```

**Expected Risk**: 65-80% (Medium-High)

### Test Input #2: Low-Risk Scenario

```
Food Type: Dairy
Storage Time: 12 hours
Temperature: 4°C (Refrigerated)
Humidity: 50%
```

**Expected Risk**: 10-20% (Low)

### Test Input #3: Medium-Risk Scenario

```
Food Type: Produce
Storage Time: 24 hours
Temperature: 18°C (Room temperature)
Humidity: 60%
```

**Expected Risk**: 30-45% (Medium)

---

## 🔬 6. Batch Data Testing

### Batch #1: Organic Lettuce Production

```
Batch ID: ORG_LETTUCE_2026_001
Crop: Leafy Greens
Farm: Sustainable Farm, Delhi
Days Since Harvest: 2
Pesticides Used: None (Organic)
Temperature: 22°C
Status: Safe for Consumption
Risk Score: 8%
Recommendation: Can be sold immediately
```

### Batch #2: Conventional Wheat

```
Batch ID: CONV_WHEAT_2026_001
Crop: Grain
Farm: Modern Farm, Punjab
Days Since Harvest: 15
Pesticides: Chlorpyrifos (applied 20 days ago)
Temperature: 32°C
Status: Marginally Safe
Risk Score: 45%
Recommendation: Use within 3 days, proper storage required
```

---

## 📊 7. Database Test Data (SQL)

### Insert Sample Agricultural Inputs

```sql
INSERT INTO agricultural_inputs (batch_id, crop_type, pesticide_used, pesticide_quantity, days_since_pesticide, fertilizer_used, fertilizer_quantity, irrigation_source, farm_location, days_since_harvest, farm_area) VALUES
('BATCH_001_WHEAT', 'grain', 'Chlorpyrifos', 1.5, 14, 'NPK 10-26-26', 50, 'groundwater', 'Maharashtra', 5, 2.5),
('BATCH_002_TOMATO', 'vegetables', 'Imidacloprid', 2.0, 7, 'Organic compost', 100, 'canal', 'Karnataka', 2, 1.2),
('BATCH_003_APPLE', 'fruits', 'Mancozeb', 3.0, 21, 'Calcium Nitrate', 75, 'river', 'Himachal Pradesh', 10, 5.0),
('BATCH_004_LETTUCE', 'leafy_greens', 'Spinosad', 0.8, 3, 'Seaweed Extract', 20, 'rain', 'Punjab', 1, 0.5),
('BATCH_005_RICE', 'grain', 'Carbofuran', 1.2, 28, 'Urea', 120, 'pumped', 'West Bengal', 8, 3.0);
```

### Insert Sample Environmental Data

```sql
INSERT INTO environmental_data (batch_id, temperature, humidity, rainfall, soil_moisture, light_exposure, wind_speed) VALUES
('BATCH_001_WHEAT', 35.5, 65, 5, 45, 10, 8),
('BATCH_002_TOMATO', 24.0, 55, 15, 60, 8, 5),
('BATCH_003_APPLE', 15.0, 40, 0, 50, 6, 3),
('BATCH_004_LETTUCE', 22.0, 70, 10, 75, 7, 2),
('BATCH_005_RICE', 28.0, 80, 20, 85, 9, 6);
```

---

## 🧪 8. API Testing with cURL

### Test Health Endpoint

```bash
curl http://localhost:5000/health
```

**Expected Response:**
```json
{
  "status": "healthy",
  "database": "connected",
  "models_loaded": true,
  "timestamp": "2026-04-15T12:00:00"
}
```

### Test Food Types Endpoint

```bash
curl http://localhost:5000/food-types
```

**Expected Response:**
```json
{
  "food_types": ["dairy", "meat", "seafood", "produce", "other"]
}
```

### Test Image Upload

```bash
curl -X POST \
  -F "image=@path/to/image.jpg" \
  http://localhost:5000/predict-image
```

### Test Risk Prediction

```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{
    "food_type": "meat",
    "storage_time": 48,
    "temperature": 28,
    "humidity": 75
  }' \
  http://localhost:5000/predict-risk
```

---

## 🎯 9. Common Test Scenarios

| Scenario | Input | Expected Output |
|----------|-------|-----------------|
| Fresh produce, cool storage | Tomato, 4°C, 12h | Safe, 5-10% risk |
| Warm meat, long storage | Chicken, 28°C, 48h | Unsafe, 80-95% risk |
| Dairy, refrigerated | Milk, 4°C, 24h | Safe, 10-15% risk |
| Organic farm, no pesticides | Lettuce, 22°C, 2h | Very Safe, <5% risk |
| Conventional, high pesticide | Wheat, 35°C, 15d post-spray | Medium, 40-50% risk |

---

## 📝 Tips for Testing

1. **Use consistent Batch IDs** - Makes tracking easier in database
2. **Test edge cases** - Very high/low temperatures, extreme storage times
3. **Mix data types** - Test different crops, pesticides, conditions
4. **Check database** - Verify data is saved in SQLite
5. **Monitor API logs** - Check terminal for request logs
6. **Test file formats** - JPG, PNG images work best

---

## 🔍 Verification Steps

After entering test data:

1. **Check Frontend**: Verify data displays correctly
2. **Check Backend**: View `agrisafe.db` in SQLite browser
3. **Monitor Logs**: Watch terminal for API requests
4. **Verify Calculations**: Confirm risk scores make sense
5. **Test API Directly**: Use cURL to bypass frontend

All sample data provided matches the actual database schema and API requirements! ✅

