# ⚡ EZINVESTER - Investment Portfolio Tracker

![Status](https://img.shields.io/badge/Status-Complete-success)
![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?logo=django&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-316192?logo=postgresql&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-7952B3?logo=bootstrap&logoColor=white)

**Live Site:** https://ezinvester-6c72f2b770d1.herokuapp.com/  
**Repository:** https://github.com/DonMarcao/ezinvester  
**Developer:** Marcus Machado  
**Project Type:** Level 5 Full Stack Web Development - Milestone 3  
**Submission Date:** April 2026

---

## 📋 Table of Contents

1. [Project Overview](#-project-overview)
2. [User Experience Design (UX)](#-user-experience-design-ux)
   - [User Stories](#user-stories)
   - [Design Process](#design-process)
   - [Wireframes](#wireframes)
   - [Color Scheme](#color-scheme)
   - [Typography](#typography)
   - [Database Schema](#database-schema)
3. [Features](#️-features)
   - [Existing Features](#existing-features)
   - [404 Page](#404-page)
   - [Features Left to Implement](#features-left-to-implement)
4. [Technologies Used](#️-technologies-used)
5. [Deployment](#-deployment)
   - [Heroku Deployment](#heroku-deployment)
   - [Local Development](#local-development)
6. [Development Process](#-development-process)
   - [Version Control Strategy](#version-control-strategy)
   - [Commit History](#commit-history)
7. [Testing](#-testing)
8. [Credits](#-credits)

---

## 🎯 Project Overview

### Overview

**EzInvester** is a full-stack investment portfolio tracker built with Django and PostgreSQL. It allows users to manage their investment assets, record dividend income, and visualise portfolio allocation through interactive charts.

- **Asset Management:** Add, edit, and delete investment assets with automatic name retrieval via yfinance
- **Dividend Tracking:** Record and manage dividend income per asset
- **Portfolio Visualisation:** Two interactive Chart.js pie charts showing allocation by asset and by type
- **User Authentication:** Secure registration, login, and logout with full user data isolation
- **Asset Type Filtering:** Filter portfolio by Stocks, ETFs, REITs, Crypto, and Treasury
- **Ticker Validation:** Real-time validation of ticker symbols via yfinance API

### Project Purpose

Developed as part of the Level 5 Diploma in Full Stack Web Development, demonstrating:

✅ **Backend Development** (Python, Django, PostgreSQL)  
✅ **User Authentication** (Django auth, session management)  
✅ **Database Design** (Relational models, migrations)  
✅ **CRUD Operations** (Full create/read/update/delete)  
✅ **External API Integration** (yfinance ticker validation)  
✅ **Data Visualisation** (Chart.js pie charts)  
✅ **Responsive Design** (Bootstrap 5, mobile-first)  
✅ **Deployment** (Heroku, WhiteNoise, dj-database-url)  
✅ **Code Quality** (PEP8 compliant, flake8 validated)  
✅ **Testing & Documentation** (Manual testing, bug tracking)

### Target Audience

1. **Individual Investors:** People managing a personal portfolio of stocks, ETFs, REITs, crypto and treasury bonds
2. **Brazilian Investors:** Users familiar with FII (Fundo de Investimento Imobiliário) and Brazilian market instruments
3. **Finance Students:** Learners who want a simple tool to track simulated portfolios
4. **Privacy-Conscious Users:** Users who prefer a self-hosted solution over commercial apps

---

## 👥 User Experience Design (UX)

### User Stories

#### 🔐 Core

| # | Story | Status |
|---|-------|--------|
| 1 | As a privacy-conscious user, I want to log in with my email and password, so that only I can access my portfolio. | ✅ |
| 2 | As an investor, I want to register for an account, so that I can start tracking my investments. | ✅ |
| 3 | As an investor, I want to add, edit, view and delete assets in my portfolio, so that I can keep my data up to date. | ✅ |
| 4 | As a beginner investor, I want to see my total amount invested on my dashboard, so that I can track my financial progress. | ✅ |
| 5 | As an investor, I want to manually record dividends received per asset, so that I can track which assets are generating income. | ✅ |
| 6 | As a beginner investor, I want the system to validate my ticker before adding an asset, so that I only add real, existing assets. | ✅ |

#### ⭐ Merit

| # | Story | Status |
|---|-------|--------|
| 7 | As an investor, I want the system to automatically fetch the asset name when I enter a ticker, so that I don't have to type everything manually. | ✅ |
| 8 | As an investor, I want to see a pie chart of my portfolio by asset type, so that I can visualise my diversification at a glance. | ✅ |
| 9 | As an investor, I want to filter my assets by type, so that I can quickly find specific investments. | ✅ |

#### 🔮 V2 (Future)

| # | Story | Status |
|---|-------|--------|
| 10 | As an investor, I want the system to automatically fetch dividend history for my assets, so that I don't have to record them manually. | 🔜 |

---

### Design Process

#### Planning
Defined data models (User → Asset → Dividend), ERD created in dbdiagram.io, user stories documented before any code was written.

#### Design Decisions

**Forms — Dedicated Pages vs Modals**

Forms for adding and editing assets and dividends were implemented as dedicated pages rather than modals. Dedicated pages are more accessible, work without JavaScript, and are easier to validate server-side. Modal implementation was considered but deprioritised to ensure ARIA compliance and robust form handling aligned with Django's built-in form system.

*Future improvement:* Convert to modal/popup in V2 for a smoother UX experience.

---

**Forms — Inline Toggle vs Dedicated Pages**

A middle-ground option was also considered: hiding forms inline on the list page, revealed via a JS toggle — avoiding full page navigation without the complexity of a modal. This approach was noted as a cleaner UX option that maintains accessibility and requires minimal JavaScript. Implementation deferred to avoid scope creep during core development.

*Future improvement:* Implement inline toggle forms in V2 as a lightweight UX enhancement before committing to full modal conversion.

---

**Visual Design Guide — AI-Generated Reference**

Prior to wireframing, AI-generated visual mockups were created as internal design reference guides to establish a consistent visual language — standardising the colour scheme (green/blue/black/white), navbar layout, typography style, and component placement.

*Tool used:* Google Gemini image generation. 9 reference images were produced covering all core pages. These were used exclusively as internal design guides and are not included in the project submission. All official wireframes were produced independently in Lucid.app.

---

### Wireframes

Wireframes created in Lucid.app during pre-project planning phase.

| Page | Wireframe |
|------|-----------|
| Login | [docs/wireframes/01_login.png](docs/wireframes/01_login.png) |
| Register | [docs/wireframes/02_register.png](docs/wireframes/02_register.png) |
| Dashboard | [docs/wireframes/03_dashboard.png](docs/wireframes/03_dashboard.png) |
| Assets List | [docs/wireframes/04_assets_list.png](docs/wireframes/04_assets_list.png) |
| Add Asset | [docs/wireframes/05_add_asset.png](docs/wireframes/05_add_asset.png) |
| Edit Asset | [docs/wireframes/06_edit_asset.png](docs/wireframes/06_edit_asset.png) |
| Dividends List | [docs/wireframes/07_dividends_list.png](docs/wireframes/07_dividends_list.png) |
| Add Dividend | [docs/wireframes/08_add_dividend.png](docs/wireframes/08_add_dividend.png) |
| 404 Page | [docs/wireframes/09_404.png](docs/wireframes/09_404.png) |

---

### Color Scheme

```css
--primary-green:    #2ecc71;   /* Brand accent, values, active states */
--dark-green:       #1a7a3f;   /* Buttons, table headers, navbar */
--background-dark:  #0a2e1a;   /* Body gradient start */
--background-mid:   #1a5c35;   /* Body gradient middle */
--card-bg:          rgba(255,255,255,0.95); /* Card backgrounds */
--stat-card-bg:     rgba(10,46,26,0.85);   /* Dashboard stat cards */
```

**Color Psychology:**
- **Green:** Growth, financial health, investment returns
- **Dark background with light cards:** Professional finance aesthetic
- **Mint background image:** Modern fintech feel

---

### Typography

**Font:** Segoe UI (system font stack)  
**Fallback:** `'Segoe UI', sans-serif`

---

### Database Schema

| Model | Field | Type |
|-------|-------|------|
| **Asset** | ticker | CharField |
| | name | CharField |
| | shares | DecimalField |
| | average_price | DecimalField |
| | asset_type | CharField (choices) |
| | purchase_date | DateField |
| **Dividend** | value | DecimalField |
| | date | DateField |

Relationships: User → Asset (one-to-many) → Dividend (one-to-many)

ERD: [docs/erd/ezinvester.png](docs/erd/ezinvester.png)

---

## ⚙️ Features

### Existing Features

#### 1. 🔐 User Authentication
- Register, login, logout
- Django session management
- Full user data isolation

#### 2. 📊 Dashboard
- Total invested, asset count, total dividends stat cards
- Portfolio by Asset pie chart (Chart.js)
- Portfolio by Type pie chart (Chart.js)
- Asset type filter buttons (All / Stock / ETF / REIT / Crypto / Treasury)
- Assets table with totals

#### 3. 💼 Asset Management (CRUD)
- Add asset with yfinance ticker validation
- Auto-fill asset name from yfinance API
- Auto-uppercase ticker input
- Edit asset details
- Delete asset with confirmation page

#### 4. 💰 Dividend Management (CRUD)
- Add dividend linked to user's assets
- Edit dividend value and date
- Delete dividend with confirmation page
- Total dividends calculated automatically

#### 5. 🎨 UI & UX
- Background image (investment-themed illustration)
- Fixed navbar with gradient
- Bootstrap 5 responsive layout
- Active filter highlighting
- Auto-dismiss alerts (4 seconds)
- form-control Bootstrap styling on all inputs
- Hamburger menu on mobile

#### 6. ♿ Accessibility
- ARIA labels on navbar and buttons
- Semantic HTML5 with `<main>` landmark
- `role="alert"` on error messages
- Keyboard navigable

### 404 Page

Custom 404 page displayed for all invalid URLs when `DEBUG=False`. Includes a "Go back to Dashboard" button.

### Features Left to Implement

- Current market price via yfinance (real-time P&L)
- Portfolio performance over time (line chart)
- Asset type lock on edit (prevent MSFT being saved as Crypto)
- Multi-currency support
- Export to CSV
- PWA / mobile app
- FII-specific metrics (dividend yield, P/VP)

---

## 🛠️ Technologies Used

### Languages
- **Python 3** — Backend logic
- **HTML5** — Templates (Django template engine)
- **CSS3** — Custom styles in style.css
- **JavaScript** — Chart.js, auto-uppercase, auto-dismiss alerts

### Frameworks & Libraries
- **Django** — Full-stack web framework
- **Bootstrap 5.3** — Responsive UI components
- **Chart.js** (CDN) — Pie charts
- **yfinance** — Ticker validation and name auto-fill
- **psycopg2** — PostgreSQL adapter
- **WhiteNoise** — Static files in production
- **dj-database-url** — Database URL parsing for Heroku
- **python-dotenv** — Environment variable management

### Database
- **PostgreSQL** — Production and local database

### Tools & Programs
- **VSCode** — Code editor
- **pgAdmin** — PostgreSQL GUI
- **Git & GitHub** — Version control
- **Heroku** — Cloud deployment
- **dbdiagram.io** — ERD creation
- **Lucid.app** — Wireframe creation
- **W3C Validator** — HTML/CSS validation
- **flake8** — Python PEP8 validation

---

## 🚀 Deployment

### Heroku Deployment

**Live Site:** https://ezinvester-6c72f2b770d1.herokuapp.com/

#### Pre-Deployment Checklist

- [x] `requirements.txt` updated (`pip freeze > requirements.txt`)
- [x] `Procfile` created
- [x] `runtime.txt` created
- [x] WhiteNoise configured in `settings.py`
- [x] `dj-database-url` configured
- [x] `DEBUG=False` for production
- [x] `ALLOWED_HOSTS` includes Heroku URL
- [x] `SECRET_KEY` set as Heroku config var
- [x] Static files collected (`python manage.py collectstatic`)

#### Deployment Steps

```bash
# 1. Install Heroku CLI and login
heroku login

# 2. Create Heroku app
heroku create ezinvester

# 3. Add PostgreSQL addon
heroku addons:create heroku-postgresql:mini

# 4. Set environment variables
heroku config:set SECRET_KEY=your-secret-key
heroku config:set DEBUG=False

# 5. Deploy
git push heroku main

# 6. Run migrations
heroku run python manage.py migrate

# 7. Open app
heroku open
```

---

### Local Development

#### Requirements

- Python 3.10+
- PostgreSQL
- Git

#### Setup

```bash
# Clone repository
git clone https://github.com/DonMarcao/ezinvester.git
cd ezinvester

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Create .env file
SECRET_KEY=your-secret-key
DEBUG=True
DB_PASSWORD=your-postgres-password

# Run migrations
python manage.py migrate

# Start server
python manage.py runserver
```

#### File Structure

```
ezinvester/
├── accounts/               # Authentication app
│   ├── views.py            # Register, login, logout views
│   └── urls.py
├── portfolio/              # Main app
│   ├── models.py           # Asset, Dividend models
│   ├── views.py            # All portfolio views
│   ├── forms.py            # AssetForm, DividendForm
│   ├── urls.py
│   └── static/
│       └── portfolio/
│           ├── css/        # style.css
│           └── images/     # Background images
├── templates/
│   ├── base.html           # Global template
│   ├── robots.txt          # SEO robots file
│   ├── accounts/           # Login, register templates
│   └── portfolio/          # Dashboard, asset, dividend templates
├── ezinvester/
│   ├── settings.py
│   └── urls.py
├── docs/
│   ├── erd/                # ezinvester.png
│   ├── wireframes/         # 01_login.png … 09_404.png
│   ├── validation/         # W3C HTML & CSS screenshots
│   └── lighthouse/         # Lighthouse mobile & desktop screenshots
├── .env                    # Environment variables (not committed)
├── .flake8                 # flake8 config
├── Procfile                # Heroku process file
├── requirements.txt
├── runtime.txt
├── manage.py
├── README.md
└── TESTING.md
```

---

## 📝 Development Process

### Version Control Strategy

**Repository:** https://github.com/DonMarcao/ezinvester  
**Primary Branch:** `main`  
**Commit Philosophy:** Small, focused commits with descriptive messages

#### Commit Message Convention

| Type | Purpose | Example |
|------|---------|---------|
| **Feat** | New feature | `Feat: Add pie charts to dashboard` |
| **Fix** | Bug fix | `Fix: Dashboard filter case mismatch` |
| **Style** | CSS/UI changes | `Style: Add background image` |
| **Refactor** | Code restructure | `Refactor: Centralise messages in base.html` |
| **Docs** | Documentation | `Docs: Add testing documentation` |
| **Test** | Testing updates | `Test: Add manual test cases` |
| **A11y** | Accessibility | `A11y: Add ARIA labels to navbar` |

### Commit History

| Commit | Description |
|--------|-------------|
| 1–4 | Project setup, documentation, wireframes |
| 5–8 | Models, authentication, dashboard |
| 9–12 | Asset CRUD, dividend CRUD, base template |
| 13–15 | yfinance validation, pie charts, filters |
| 16–17 | JS enhancements, ARIA accessibility |
| 18–19 | Visual polish, UI fixes |
| 20–22 | PEP8 compliance, comments, flake8 |
| 23–24 | Testing documentation, responsiveness suite |
| 25–27 | Production config: WhiteNoise, dj-database-url, Procfile |
| 28–29 | Heroku deploy, smoke tests, static files |
| 30 | SEO improvements: meta description, robots.txt |
| 31 | Accessibility: main landmark added to base.html |
| 32 | Final README and TESTING.md update |

---

## 🧪 Testing

**Comprehensive testing documentation:** [TESTING.md](TESTING.md)

### Quick Stats

- **Total Tests:** 53
- **Pass Rate:** 100% (53/53)
- **Critical Bugs:** 0
- **Python:** 0 flake8 errors
- **HTML:** 0 W3C errors (9 templates)
- **CSS:** 0 W3C errors

### Lighthouse Scores (Dashboard — Live Site)

| Category | Mobile | Desktop |
|----------|--------|---------|
| Performance | 96 | 99 |
| Accessibility | 100 | 100 |
| Best Practices | 100 | 100 |
| SEO | 100 | 100 |

Screenshots: [Mobile](docs/lighthouse/lighthouse_mobile_validator.png) | [Desktop](docs/lighthouse/lighthouse_desktop_validator.png)

### W3C Validation

| Template | Screenshot |
|----------|------------|
| Login | [docs/validation/login_validator.png](docs/validation/login_validator.png) |
| Register | [docs/validation/register_validator.png](docs/validation/register_validator.png) |
| Dashboard | [docs/validation/dashboard_validator.png](docs/validation/dashboard_validator.png) |
| Asset List | [docs/validation/asset_list_validator.png](docs/validation/asset_list_validator.png) |
| Add Asset | [docs/validation/asset_add_validator.png](docs/validation/asset_add_validator.png) |
| Edit Asset | [docs/validation/asset_edit_validator.png](docs/validation/asset_edit_validator.png) |
| Delete Asset | [docs/validation/asset_delete_validator.png](docs/validation/asset_delete_validator.png) |
| Dividends List | [docs/validation/dividends_list_validator.png](docs/validation/dividends_list_validator.png) |
| Add Dividend | [docs/validation/dividends_add_validator.png](docs/validation/dividends_add_validator.png) |
| Edit Dividend | [docs/validation/dividends_edit_validator.png](docs/validation/dividends_edit_validator.png) |
| Delete Dividend | [docs/validation/dividends_delete_validator.png](docs/validation/dividends_delete_validator.png) |
| 404 Page | [docs/validation/404_validator.png](docs/validation/404_validator.png) |
| CSS | [docs/validation/css_validator.png](docs/validation/css_validator.png) |

### Test Coverage

- ✅ Authentication (6 tests)
- ✅ Asset CRUD (10 tests)
- ✅ Asset Filtering (7 tests)
- ✅ Dividend CRUD (5 tests)
- ✅ Dashboard (6 tests)
- ✅ Navigation & Security (6 tests)
- ✅ UI & Alerts (5 tests)
- ✅ Responsiveness (8 tests)

---

## 🙏 Credits

### Code Attribution

**yfinance Integration**
- Library: yfinance by Ran Aroussi
- License: Apache 2.0
- Source: https://github.com/ranaroussi/yfinance
- Usage: Ticker validation and asset name auto-fill

**Chart.js**
- Library: Chart.js
- License: MIT
- Source: https://www.chartjs.org/
- Usage: Portfolio pie charts

**Bootstrap 5.3**
- Framework: Bootstrap
- License: MIT
- Source: https://getbootstrap.com/
- Usage: Responsive UI components

**dj-database-url**
- Library: dj-database-url
- License: BSD
- Source: https://github.com/jazzband/dj-database-url
- Usage: Heroku PostgreSQL URL parsing

**WhiteNoise**
- Library: WhiteNoise
- License: MIT
- Source: http://whitenoise.evans.io/
- Usage: Static file serving in production

### Original Implementation

All application logic, features and implementations created by Marcus Machado, including:
- Django models, views, forms and URL configuration
- User authentication and data isolation logic
- yfinance ticker validation and name auto-fill
- Chart.js data preparation and rendering
- Asset type filtering on dashboard and asset list
- Bootstrap 5 responsive layout and custom CSS
- JavaScript enhancements (auto-uppercase, auto-dismiss alerts)
- Heroku deployment configuration

### Acknowledgments

- **Code Institute** — Level 5 Full Stack Web Development course
- **Django Documentation** — https://docs.djangoproject.com/
- **Bootstrap Documentation** — https://getbootstrap.com/docs/
- **Chart.js Documentation** — https://www.chartjs.org/docs/
- **Stack Overflow Community** — Problem-solving assistance

---

## 📄 License

MIT License — Copyright (c) 2026 Marcus Machado

---

**Developer:** Marcus Machado  
**GitHub:** [@DonMarcao](https://github.com/DonMarcao)  
**Status:** ✅ Live on Heroku

---

⭐ **[View Complete Testing Documentation →](TESTING.md)** ⭐