# ShambaOps (Django + Bootstrap)

A Kenya-focused Country Living Operations system with separate apps:
- Organic farming
- Poultry
- Seed propagation
- Nursery management
- Kitchen gardening
- Landscaping
- Beekeeping
- Repairs
- Machine & tool preventive maintenance
- Inventory
- Finance
- Core (locations, people, suppliers, assets, tasks)

## Quick start

```bash
python -m venv venv
# Windows: venv\Scripts\activate
# Linux/macOS: source venv/bin/activate
pip install -r requirements.txt

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Open:
- App: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

Notes:
- Create/Edit/Delete are staff-only (requires login + is_staff).
- List/Detail are readable once logged in (Login required for write pages only; list pages are public by default).
