# نموذج البيانات المقترح

| الكيان | أهم الحقول |
|---|---|
| Vehicle (مركبة) | id, plate, type, owner_company_id, inspection_expiry, tracker_id |
| Driver (سائق) | id, license_no, hazmat_permit_expiry, hours_driven_today |
| Company (شركة) | id, name, license_no |
| Shipment (شحنة) | id, vehicle_id, driver_id, material_class (UN class), un_number, origin, destination, planned_route |
| Position (موقع) | shipment_id, timestamp, lat, lon, speed_kmh, heading |
| RiskEvent (حدث خطر) | id, shipment_id, type, score, reasons[], created_at |
| Alert (تنبيه) | id, risk_event_id, level, target_agency, status, handled_at |
| Agency (جهة) | id, name, type (traffic, ambulance, civil_defense, regulator) |
| Incident (حادثة) | id, location, time, shipments_involved[], severity, notes |

المرجع الدولي لتصنيف المواد الخطرة: تصنيف الأمم المتحدة (فئات 1 إلى 9). يجب مراجعة المتطلبات القانونية المصرية مع الجهات المختصة.
