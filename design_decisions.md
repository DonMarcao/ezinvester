## Design Decisions

### Forms — Dedicated Pages vs Modals
Forms for adding and editing assets and dividends 
were implemented as dedicated pages rather than 
modals/popups.

**Reason:** Dedicated pages are more accessible, 
work without JavaScript, and are easier to validate 
server-side. Modal implementation was considered 
but deprioritised to ensure ARIA compliance and 
robust form handling aligned with Django's 
built-in form system.

**Future improvement:** Convert to modal/popup 
in V2 for a smoother UX experience.

---

### Forms — Inline Toggle vs Dedicated Pages
A middle-ground option was considered: hiding 
forms inline on the list page, revealed via a 
simple JS toggle — avoiding full page navigation 
without the complexity of a modal.

**Reason:** This approach was noted as a cleaner 
UX option that maintains accessibility and requires 
minimal JavaScript. Implementation deferred to 
avoid scope creep during core development.

**Future improvement:** Implement inline toggle 
forms in V2 as a lightweight UX enhancement 
before committing to full modal conversion.

---

### Visual Design Guide — AI-Generated Reference
Prior to building wireframes in Balsamiq, AI-generated 
visual mockups were created as design reference guides.

**Reason:** To establish a consistent visual language 
across all pages before wireframing — standardising previosly selected
colour scheme (green/blue/black/white), navbar layout, typography 
style, and component placement.

**Tool used:** Google Gemini image generation.

**Outcome:** 9 reference images were produced covering 
all core pages. These were used exclusively as internal 
design guides and do not represent the final UI. 
All official wireframes were produced independently 
in Balsamiq.

**Attribution:** AI-generated images were used as 
visual reference only and are not included in the 
project submission.