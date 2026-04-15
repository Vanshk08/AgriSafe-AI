## 🥬 Agricultural Input Data for AgriSafe AI

Complete sample data for testing agricultural contamination detection system.

---

## 📋 Agricultural Input Form Fields

When entering data, use these fields:

| Field | Type | Example | Description |
|-------|------|---------|-------------|
| **Batch ID** | String | BATCH_001 | Unique identifier for the batch |
| **Crop Type** | Dropdown | grain, vegetables, fruits, legumes, herbs, spices, nuts, root_crops, leafy_greens, other | Type of crop |
| **Pesticide Used** | String | Chlorpyrifos | Name of pesticide applied |
| **Pesticide Quantity** | Float | 1.5 | Quantity in kg/hectare |
| **Days Since Pesticide** | Integer | 14 | Days since pesticide application |
| **Fertilizer Used** | String | NPK 10-26-26 | Type of fertilizer |
| **Fertilizer Quantity** | Float | 50 | Quantity in kg/hectare |
| **Irrigation Source** | Dropdown | groundwater, rain, river, pumped, well, canal | Water source |
| **Farm Location** | String | Maharashtra, India | Geographic location |
| **Days Since Harvest** | Integer | 5 | Days post-harvest |
| **Farm Area** | Float | 2.5 | Size in hectares |

---

## 📊 Sample Batch Data - Ready to Use

### ✅ **Batch #1: Low-Risk Wheat Farm (SAFE)**

```
Batch ID: BATCH_WHEAT_001
Crop Type: grain
Pesticide Used: Chlorpyrifos (Conventional)
Pesticide Quantity: 1.5 kg/hectare
Days Since Pesticide: 25 days (Safe - 14 days min)
Fertilizer Used: NPK 10-26-26
Fertilizer Quantity: 50 kg/hectare
Irrigation Source: groundwater
Farm Location: Punjab, India
Days Since Harvest: 15 days
Farm Area: 3.5 hectares

Expected Risk Score: 20-30% (LOW)
Recommendation: SAFE FOR CONSUMPTION
```

---

### ✅ **Batch #2: Medium-Risk Tomato Farm (CAUTION)**

```
Batch ID: BATCH_TOMATO_002
Crop Type: vegetables
Pesticide Used: Imidacloprid
Pesticide Quantity: 2.0 kg/hectare
Days Since Pesticide: 7 days (Too Soon!)
Fertilizer Used: Organic compost
Fertilizer Quantity: 100 kg/hectare
Irrigation Source: canal
Farm Location: Karnataka, India
Days Since Harvest: 2 days
Farm Area: 1.2 hectares

Expected Risk Score: 50-65% (MEDIUM)
Recommendation: USE WITHIN 3 DAYS WITH PROPER STORAGE
```

---

### ✅ **Batch #3: Low-Risk Apple Orchard (SAFE)**

```
Batch ID: BATCH_APPLE_003
Crop Type: fruits
Pesticide Used: Mancozeb (Fungicide)
Pesticide Quantity: 3.0 kg/hectare
Days Since Pesticide: 25 days (Safe)
Fertilizer Used: Calcium Nitrate
Fertilizer Quantity: 75 kg/hectare
Irrigation Source: river
Farm Location: Himachal Pradesh, India
Days Since Harvest: 12 days
Farm Area: 5.0 hectares

Expected Risk Score: 25-35% (LOW)
Recommendation: SAFE - GOOD STORAGE CONDITIONS
```

---

### ✅ **Batch #4: Very Low-Risk Lettuce Farm (VERY SAFE)**

```
Batch ID: BATCH_LETTUCE_004
Crop Type: leafy_greens
Pesticide Used: Spinosad (Organic)
Pesticide Quantity: 0.8 kg/hectare
Days Since Pesticide: 5 days
Fertilizer Used: Seaweed Extract (Organic)
Fertilizer Quantity: 20 kg/hectare
Irrigation Source: rain
Farm Location: Punjab, India
Days Since Harvest: 1 day (Very Fresh!)
Farm Area: 0.5 hectares

Expected Risk Score: 5-15% (VERY LOW)
Recommendation: EXCELLENT - CONSUME IMMEDIATELY
```

---

### ⚠️ **Batch #5: High-Risk Rice Paddy (UNSAFE)**

```
Batch ID: BATCH_RICE_005
Crop Type: grain
Pesticide Used: Carbofuran (Highly Toxic)
Pesticide Quantity: 1.2 kg/hectare
Days Since Pesticide: 5 days (TOO SOON!)
Fertilizer Used: Urea (46-0-0) - Heavy application
Fertilizer Quantity: 120 kg/hectare (Excessive)
Irrigation Source: pumped
Farm Location: West Bengal, India
Days Since Harvest: 3 days (Too recent)
Farm Area: 3.0 hectares

Expected Risk Score: 75-85% (HIGH)
Recommendation: NOT SAFE YET - WAIT 10+ DAYS
```

---

## 🚜 Additional Sample Batches

### Batch #6: Root Vegetables (Medium Risk)

```
Batch ID: BATCH_ROOT_006
Crop Type: root_crops
Pesticide Used: Thiram
Pesticide Quantity: 2.5 kg/hectare
Days Since Pesticide: 10 days
Fertilizer Used: Composted manure
Fertilizer Quantity: 40 kg/hectare
Irrigation Source: well
Farm Location: Rajasthan, India
Days Since Harvest: 6 days
Farm Area: 2.0 hectares

Expected Risk: 35-45% (MEDIUM)
```

---

### Batch #7: Herb Farm (Low Risk)

```
Batch ID: BATCH_HERBS_007
Crop Type: herbs
Pesticide Used: Neem oil (Organic)
Pesticide Quantity: 0.5 kg/hectare
Days Since Pesticide: 3 days
Fertilizer Used: Vermicompost
Fertilizer Quantity: 10 kg/hectare
Irrigation Source: drip irrigation
Farm Location: Goa, India
Days Since Harvest: 0 days (Just harvested)
Farm Area: 0.3 hectares

Expected Risk: 8-12% (VERY LOW)
```

---

### Batch #8: Nut Farm (Low Risk)

```
Batch ID: BATCH_NUTS_008
Crop Type: nuts
Pesticide Used: Pyrethrins (Natural)
Pesticide Quantity: 1.0 kg/hectare
Days Since Pesticide: 18 days
Fertilizer Used: Balanced NPK
Fertilizer Quantity: 60 kg/hectare
Irrigation Source: groundwater
Farm Location: Maharashtra, India
Days Since Harvest: 20 days
Farm Area: 4.0 hectares

Expected Risk: 15-25% (LOW)
```

---

## 🔬 Testing Strategy

### Test Scenario 1: Safe Produce Path
Use: **BATCH_WHEAT_001**, **BATCH_APPLE_003**, **BATCH_LETTUCE_004**
Expected: All pass safety checks ✅

### Test Scenario 2: Caution Zone Path
Use: **BATCH_TOMATO_002**, **BATCH_ROOT_006**
Expected: Warnings, recommendations for proper storage ⚠️

### Test Scenario 3: Unsafe Path
Use: **BATCH_RICE_005**
Expected: Fail safety checks, recommend waiting ❌

### Test Scenario 4: Organic Certification Path
Use: **BATCH_LETTUCE_004**, **BATCH_HERBS_007**
Expected: Clean data, very low risk scores ✅

---

## 📝 How to Input in UI

### Step-by-Step for BATCH_WHEAT_001:

1. **Batch ID**: Type `BATCH_WHEAT_001`
2. **Crop Type**: Select `grain`
3. **Pesticide Used**: Type `Chlorpyrifos`
4. **Pesticide Quantity**: Enter `1.5`
5. **Days Since Pesticide**: Enter `25`
6. **Fertilizer Used**: Type `NPK 10-26-26`
7. **Fertilizer Quantity**: Enter `50`
8. **Irrigation Source**: Select `groundwater`
9. **Farm Location**: Type `Punjab, India`
10. **Days Since Harvest**: Enter `15`
11. **Farm Area**: Enter `3.5`
12. **Submit** → Check results

---

## 💾 SQL Insert Statements

Paste this in SQLite to load all sample batches:

```sql
INSERT INTO agricultural_inputs (batch_id, crop_type, pesticide_used, pesticide_quantity, days_since_pesticide, fertilizer_used, fertilizer_quantity, irrigation_source, farm_location, days_since_harvest, farm_area) VALUES
('BATCH_WHEAT_001', 'grain', 'Chlorpyrifos', 1.5, 25, 'NPK 10-26-26', 50, 'groundwater', 'Punjab, India', 15, 3.5),
('BATCH_TOMATO_002', 'vegetables', 'Imidacloprid', 2.0, 7, 'Organic compost', 100, 'canal', 'Karnataka, India', 2, 1.2),
('BATCH_APPLE_003', 'fruits', 'Mancozeb', 3.0, 25, 'Calcium Nitrate', 75, 'river', 'Himachal Pradesh, India', 12, 5.0),
('BATCH_LETTUCE_004', 'leafy_greens', 'Spinosad', 0.8, 5, 'Seaweed Extract', 20, 'rain', 'Punjab, India', 1, 0.5),
('BATCH_RICE_005', 'grain', 'Carbofuran', 1.2, 5, 'Urea', 120, 'pumped', 'West Bengal, India', 3, 3.0),
('BATCH_ROOT_006', 'root_crops', 'Thiram', 2.5, 10, 'Composted manure', 40, 'well', 'Rajasthan, India', 6, 2.0),
('BATCH_HERBS_007', 'herbs', 'Neem oil', 0.5, 3, 'Vermicompost', 10, 'drip irrigation', 'Goa, India', 0, 0.3),
('BATCH_NUTS_008', 'nuts', 'Pyrethrins', 1.0, 18, 'Balanced NPK', 60, 'groundwater', 'Maharashtra, India', 20, 4.0);
```

---

## ✅ Verification Checklist

After entering data:
- [ ] Data appears in database
- [ ] Risk scores calculated
- [ ] Recommendations generated
- [ ] Environmental data linked
- [ ] Batch history tracked

Start with **BATCH_LETTUCE_004** (simplest, safest) and progress to **BATCH_RICE_005** (most complex, highest risk)! 🚀
