import React, { useEffect, useMemo, useState } from 'react';
import { createRoot } from 'react-dom/client';
import {
  BadgeCheck,
  BarChart3,
  CalendarClock,
  CheckCircle2,
  ClipboardList,
  CreditCard,
  Eye,
  Gauge,
  Globe2,
  MessageCircle,
  Phone,
  Plus,
  Send,
  Settings,
  Share2,
  Users,
} from 'lucide-react';
import { api } from './api';
import { personaPacks, starterBusinesses } from './sampleData';
import './styles.css';

const STORAGE_KEY = 'bizznexx_workspace_v1';

const ownerViews = [
  { id: 'today', label: 'Today', icon: CalendarClock },
  { id: 'leads', label: 'Leads', icon: Users },
  { id: 'payments', label: 'Payments', icon: CreditCard },
  { id: 'catalogue', label: 'Catalogue', icon: Globe2 },
  { id: 'messages', label: 'Messages', icon: MessageCircle },
  { id: 'insights', label: 'Insights', icon: BarChart3 },
];

const operatorViews = [{ id: 'setup', label: 'Setup', icon: Settings }];

function App() {
  const [businesses, setBusinesses] = useState(loadBusinesses);
  const [selectedId, setSelectedId] = useState(businesses[0]?.id);
  const [view, setView] = useState('today');
  const [operatorMode, setOperatorMode] = useState(false);
  const [apiMode, setApiMode] = useState('loading');
  const [messageDraft, setMessageDraft] = useState(null);

  const selected = ensureBusinessDefaults(
    businesses.find((business) => business.id === selectedId) || businesses[0] || starterBusinesses[0],
  );

  async function refreshBusinesses(preferredId = selectedId) {
    try {
      const records = await api.getBusinesses();
      const normalized = records.map(normalizeBusiness);
      setBusinesses(normalized);
      setSelectedId(normalized.find((business) => business.id === preferredId)?.id || normalized[0]?.id);
      setApiMode('api');
    } catch {
      setApiMode('local');
    }
  }

  useEffect(() => {
    refreshBusinesses();
  }, []);

  useEffect(() => {
    if ('serviceWorker' in navigator) {
      navigator.serviceWorker.register('/sw.js').catch(() => {});
    }
  }, []);

  useEffect(() => {
    if (apiMode === 'local') {
      localStorage.setItem(STORAGE_KEY, JSON.stringify(businesses));
    }
  }, [apiMode, businesses]);

  function updateBusiness(nextBusiness) {
    setBusinesses((current) =>
      current.map((business) => (business.id === nextBusiness.id ? ensureBusinessDefaults(nextBusiness) : business)),
    );
  }

  async function createInquiry(payload) {
    if (apiMode === 'api') {
      const result = await api.captureInquiry({
        business: selected.id,
        catalogue_item: payload.catalogueItemId,
        name: payload.name,
        phone_number: payload.phone,
        message: payload.note,
        source: payload.source,
        expected_value: payload.expectedAmount || 0,
        extra_context: {
          detail_one: payload.detailOne,
          detail_two: payload.detailTwo,
        },
      });
      await refreshBusinesses(result.lead.business);
      setView('today');
      return;
    }

    const pack = personaPacks[selected.pack];
    const nextLead = {
      id: `lead_${Date.now()}`,
      name: payload.name,
      phone: payload.phone,
      service: payload.service,
      source: payload.source,
      status: pack.statuses[0],
      nextAction: 'Send first response and schedule next step',
      amount: payload.expectedAmount || 0,
      followUpAgeDays: 0,
      urgencyReason: 'New inquiry from public page.',
    };
    updateBusiness({ ...selected, leads: [nextLead, ...selected.leads] });
    setView('today');
  }

  const learningStudioViews = selected.pack === 'tutor' ? [{ id: 'learningStudioBeta', label: 'Beta Studio', icon: BadgeCheck }] : [];
  const nav = operatorMode ? [...learningStudioViews, ...ownerViews, ...operatorViews] : [...learningStudioViews, ...ownerViews];

  useEffect(() => {
    if (selected.pack !== 'tutor' && view === 'learningStudioBeta') {
      setView('today');
    }
  }, [selected.pack, view]);

  return (
    <div className="workspace-shell">
      <aside className="sidebar">
        <Brand />
        <BusinessPicker businesses={businesses} selectedId={selected.id} onSelect={setSelectedId} />
        <nav className="nav-list">
          {nav.map((item) => {
            const Icon = item.icon;
            return (
              <button
                className={view === item.id ? 'nav-item active' : 'nav-item'}
                key={item.id}
                onClick={() => setView(item.id)}
              >
                <Icon size={18} />
                <span>{item.label}</span>
              </button>
            );
          })}
        </nav>
        <button className="operator-toggle" onClick={() => setOperatorMode((current) => !current)}>
          <Settings size={16} />
          {operatorMode ? 'Hide operator tools' : 'Operator mode'}
        </button>
        <div className="sidebar-note">
          <span>Status</span>
          <strong>{apiMode === 'api' ? 'API connected' : apiMode === 'loading' ? 'Connecting' : 'Local fallback'}</strong>
        </div>
      </aside>

      <main className="main-panel">
        <WorkspaceHeader business={selected} />
        {view === 'learningStudioBeta' && (
          <LearningStudioBetaView
            business={selected}
            apiMode={apiMode}
            refreshBusinesses={refreshBusinesses}
            updateBusiness={updateBusiness}
            onInquiry={createInquiry}
            onDraft={setMessageDraft}
          />
        )}
        {view === 'today' && (
          <TodayView
            business={selected}
            apiMode={apiMode}
            refreshBusinesses={refreshBusinesses}
            updateBusiness={updateBusiness}
            onDraft={setMessageDraft}
          />
        )}
        {view === 'leads' && (
          <LeadsView
            business={selected}
            apiMode={apiMode}
            refreshBusinesses={refreshBusinesses}
            updateBusiness={updateBusiness}
            onDraft={setMessageDraft}
          />
        )}
        {view === 'payments' && (
          <PaymentsView
            business={selected}
            apiMode={apiMode}
            refreshBusinesses={refreshBusinesses}
            updateBusiness={updateBusiness}
            onDraft={setMessageDraft}
          />
        )}
        {view === 'catalogue' && <CatalogueWorkspace business={selected} onInquiry={createInquiry} />}
        {view === 'messages' && <MessagesView business={selected} />}
        {view === 'insights' && <InsightsView business={selected} />}
        {view === 'setup' && operatorMode && (
          <OperatorSetup
            business={selected}
            businesses={businesses}
            apiMode={apiMode}
            refreshBusinesses={refreshBusinesses}
            updateBusiness={updateBusiness}
          />
        )}
      </main>

      {messageDraft && <MessagePreview business={selected} draft={messageDraft} onClose={() => setMessageDraft(null)} />}
    </div>
  );
}

function Brand() {
  return (
    <div className="brand-lockup">
      <div className="brand-mark">BN</div>
      <div>
        <strong>BizzNexx</strong>
        <span>Business workspace</span>
      </div>
    </div>
  );
}

function BusinessPicker({ businesses, selectedId, onSelect }) {
  return (
    <label className="business-picker">
      <span>Business</span>
      <select value={selectedId} onChange={(event) => onSelect(coerceId(event.target.value))}>
        {businesses.map((business) => (
          <option value={business.id} key={business.id}>
            {business.name}
          </option>
        ))}
      </select>
    </label>
  );
}

function WorkspaceHeader({ business }) {
  return (
    <header className="workspace-header">
      <div>
        <p className="eyebrow">{personaPacks[business.pack]?.label || business.pack}</p>
        <h1>{business.name}</h1>
        <span>
          {business.owner} · {business.city} · {business.setupStage}
        </span>
      </div>
      <div className="header-actions">
        <button className="ghost-button" onClick={() => navigator.clipboard?.writeText(publicUrl(business))}>
          <Share2 size={16} />
          Copy link
        </button>
        <a className="primary-button" href={whatsAppHref(business, `Hi, I want to know more about ${business.name}`)}>
          <MessageCircle size={16} />
          WhatsApp
        </a>
      </div>
    </header>
  );
}

function LearningStudioBetaView({ business, apiMode, refreshBusinesses, updateBusiness, onInquiry, onDraft }) {
  const [form, setForm] = useState(defaultInquiryForm(business));
  const stats = getStats(business);
  const pendingPayments = business.payments.filter((payment) => payment.status !== 'Paid');
  const trialLeads = business.leads.filter((lead) =>
    `${lead.status} ${lead.nextAction}`.toLowerCase().includes('trial'),
  );
  const priorityLeads = (trialLeads.length ? trialLeads : business.leads).slice(0, 4);

  useEffect(() => {
    setForm(defaultInquiryForm(business));
  }, [business.id]);

  function submit(event) {
    event.preventDefault();
    if (!form.name || !form.phone) return;
    const selectedItem = business.catalogue.items.find((item) => String(item.id) === String(form.catalogueItemId));
    onInquiry({
      ...form,
      service: selectedItem?.name || '',
      source: 'Learning Studio beta page',
      expectedAmount: parseAmount(selectedItem?.price),
    });
    setForm(defaultInquiryForm(business));
  }

  return (
    <section className="studio-beta">
      <div className="studio-beta-banner">
        <div>
          <p className="eyebrow">Parallel beta build</p>
          <h2>Learning Studio experience for parent trust, trial follow-up, and monthly fee discipline.</h2>
          <span>
            This tab reuses the existing BizzNexx workflow while testing a sharper tutor-specific product surface.
          </span>
        </div>
        <div className="studio-beta-stats">
          <Metric icon={Users} label="Open parent inquiries" value={stats.openLeads} tone="yellow" />
          <Metric icon={CreditCard} label="Pending fees" value={`Rs. ${stats.pendingAmount.toLocaleString('en-IN')}`} tone="rose" />
        </div>
      </div>

      <div className="studio-beta-safety">
        <BadgeCheck size={18} />
        <span>
          Beta note: this page uses demo-ready learning studio data. BizzNexx tracks inquiries, follow-ups, and fee
          status only; it does not guarantee marks, admissions, lead volume, payment recovery, or legal compliance.
        </span>
      </div>

      <div className="studio-parent-page">
        <section className="studio-hero">
          <div>
            <p className="eyebrow">Parent-ready public page</p>
            <h1>{business.catalogue.headline}</h1>
            <p>{business.catalogue.subtext}</p>
            <div className="public-actions">
              <a
                className="primary-button"
                href={whatsAppHref(
                  business,
                  `Hi, I want to discuss a trial class at ${business.name}. Student class/board: `,
                )}
              >
                <MessageCircle size={16} />
                Ask on WhatsApp
              </a>
              <button className="ghost-button" onClick={() => navigator.clipboard?.writeText(publicUrl(business))}>
                <Share2 size={16} />
                Copy parent link
              </button>
            </div>
          </div>
          <aside className="teacher-card">
            <span>Teacher profile</span>
            <strong>{business.owner}</strong>
            <p>
              8 years of Maths and Science coaching for CBSE, ICSE, and WB board students, with patient doubt clearing
              and monthly parent updates.
            </p>
          </aside>
        </section>

        <section className="studio-proof-grid">
          {business.proof.map((item) => (
            <div className="studio-proof" key={item}>
              <BadgeCheck size={18} />
              <span>{item}</span>
            </div>
          ))}
        </section>

        <section className="studio-section">
          <SectionTitle eyebrow="Classes and fees" title="Choose the right support path" />
          <div className="studio-course-grid">
            {business.catalogue.items.map((item) => (
              <article className="studio-course-card" key={item.id}>
                <span>{item.format}</span>
                <h3>{item.name}</h3>
                <p>{item.description}</p>
                {item.details && <small>{item.details}</small>}
                {item.timingOrTimeline && <small>{item.timingOrTimeline}</small>}
                {item.terms && <small>{item.terms}</small>}
                <strong>{item.price}</strong>
              </article>
            ))}
          </div>
        </section>

        <section className="studio-section two-column">
          <div>
            <SectionTitle eyebrow="Trial inquiry" title="Capture parent context before WhatsApp" />
            <form className="inquiry-form studio-inquiry" onSubmit={submit}>
              <input
                placeholder="Parent / student name"
                value={form.name}
                onChange={(event) => setForm({ ...form, name: event.target.value })}
              />
              <input
                placeholder="Phone number"
                value={form.phone}
                onChange={(event) => setForm({ ...form, phone: event.target.value })}
              />
              <select
                value={form.catalogueItemId}
                onChange={(event) => setForm({ ...form, catalogueItemId: event.target.value })}
              >
                {business.catalogue.items.map((item) => (
                  <option value={item.id} key={item.id}>
                    {item.name}
                  </option>
                ))}
              </select>
              <input
                placeholder="Class and board, e.g. Class 10 ICSE"
                value={form.detailOne}
                onChange={(event) => setForm({ ...form, detailOne: event.target.value })}
              />
              <input
                placeholder="Subject concern and preferred timing"
                value={form.detailTwo}
                onChange={(event) => setForm({ ...form, detailTwo: event.target.value })}
              />
              <textarea
                placeholder="Anything the parent wants the teacher to know"
                value={form.note}
                onChange={(event) => setForm({ ...form, note: event.target.value })}
              />
              <button className="primary-button" type="submit">
                <Send size={16} />
                Send trial inquiry
              </button>
              <small>Parent details are used only to respond to this inquiry during beta validation.</small>
            </form>
          </div>

          <div className="studio-process">
            <SectionTitle eyebrow="What happens next" title="Simple, reassuring parent journey" />
            {[
              'Parent shares class, board, subject, and timing.',
              'Ananya sends trial options on WhatsApp.',
              'Trial reminder appears before the session.',
              'Post-trial follow-up and fee plan are tracked.',
            ].map((step, index) => (
              <div className="studio-step" key={step}>
                <strong>{index + 1}</strong>
                <span>{step}</span>
              </div>
            ))}
          </div>
        </section>

        <section className="studio-section two-column">
          <Panel title="Parent-trial action queue">
            <LeadActionList
              business={business}
              leads={priorityLeads}
              apiMode={apiMode}
              refreshBusinesses={refreshBusinesses}
              updateBusiness={updateBusiness}
              onDraft={onDraft}
            />
          </Panel>
          <Panel title="Monthly fee actions">
            <PaymentActionList
              business={business}
              payments={pendingPayments}
              apiMode={apiMode}
              refreshBusinesses={refreshBusinesses}
              updateBusiness={updateBusiness}
              onDraft={onDraft}
            />
          </Panel>
        </section>

        <section className="studio-section">
          <SectionTitle eyebrow="Parent FAQ" title="Questions that reduce repeated explanation" />
          <div className="faq-grid">
            {business.catalogue.faqs.map((faq) => (
              <article className="faq-card" key={faq.question || faq}>
                <strong>{faq.question || faq}</strong>
                {faq.answer && <p>{faq.answer}</p>}
              </article>
            ))}
          </div>
        </section>
      </div>
    </section>
  );
}

function TodayView({ business, apiMode, refreshBusinesses, updateBusiness, onDraft }) {
  const stats = getStats(business);
  const urgentLeads = business.leads.slice().sort((a, b) => (b.followUpAgeDays || 0) - (a.followUpAgeDays || 0));
  const urgentPayments = business.payments
    .filter((payment) => payment.status !== 'Paid')
    .slice()
    .sort((a, b) => (b.ageDays || 0) - (a.ageDays || 0));

  return (
    <section className="page-stack">
      <div className="hero-band">
        <div>
          <p className="eyebrow">Today</p>
          <h2>
            {stats.openLeads} open leads, {stats.followUps} follow-ups, Rs.{' '}
            {stats.pendingAmount.toLocaleString('en-IN')} pending.
          </h2>
          <span>Start with the urgent action queue. The owner should not need to hunt through reports.</span>
        </div>
        <div className="hero-actions">
          <button className="ghost-button" onClick={() => navigator.clipboard?.writeText(publicUrl(business))}>
            <Share2 size={16} />
            Share page
          </button>
        </div>
      </div>

      <div className="metric-grid">
        <Metric icon={Gauge} label="Growth Score" value={`${business.growthScore}/100`} tone="green" />
        <Metric icon={CheckCircle2} label="Health Score" value={`${business.healthScore}/100`} tone="blue" />
        <Metric icon={Users} label="Open Leads" value={stats.openLeads} tone="yellow" />
        <Metric icon={CreditCard} label="Pending" value={`Rs. ${stats.pendingAmount.toLocaleString('en-IN')}`} tone="rose" />
      </div>

      <div className="two-column">
        <Panel title="Urgent lead actions">
          <LeadActionList
            business={business}
            leads={urgentLeads}
            apiMode={apiMode}
            refreshBusinesses={refreshBusinesses}
            updateBusiness={updateBusiness}
            onDraft={onDraft}
          />
        </Panel>
        <Panel title="Payment actions">
          <PaymentActionList
            business={business}
            payments={urgentPayments}
            apiMode={apiMode}
            refreshBusinesses={refreshBusinesses}
            updateBusiness={updateBusiness}
            onDraft={onDraft}
          />
        </Panel>
      </div>

      <Panel title="What changed and why it matters">
        <div className="reason-grid">
          {business.scoreReasons.map((reason) => (
            <article className={`reason-card ${reason.severity}`} key={reason.label}>
              <strong>{reason.label}</strong>
              <span>{reason.detail}</span>
            </article>
          ))}
        </div>
      </Panel>
    </section>
  );
}

function LeadsView({ business, apiMode, refreshBusinesses, updateBusiness, onDraft }) {
  return (
    <section className="page-stack">
      <SectionTitle eyebrow="Lead operations" title="Every inquiry needs a next action" />
      <Panel title="Lead queue">
        <LeadActionList
          business={business}
          leads={business.leads}
          apiMode={apiMode}
          refreshBusinesses={refreshBusinesses}
          updateBusiness={updateBusiness}
          onDraft={onDraft}
        />
      </Panel>
    </section>
  );
}

function PaymentsView({ business, apiMode, refreshBusinesses, updateBusiness, onDraft }) {
  return (
    <section className="page-stack">
      <SectionTitle eyebrow="Receivables" title="Track money without becoming accounting software" />
      <Panel title="Payment queue">
        <PaymentActionList
          business={business}
          payments={business.payments}
          apiMode={apiMode}
          refreshBusinesses={refreshBusinesses}
          updateBusiness={updateBusiness}
          onDraft={onDraft}
        />
      </Panel>
    </section>
  );
}

function CatalogueWorkspace({ business, onInquiry }) {
  return (
    <section className="page-stack">
      <SectionTitle eyebrow="Catalogue and page" title="Preview, improve, and share the public business page" />
      <div className="catalogue-actions">
        <span>Public URL: {publicUrl(business)}</span>
        <button className="ghost-button" onClick={() => navigator.clipboard?.writeText(publicUrl(business))}>
          <Share2 size={16} />
          Copy share link
        </button>
      </div>
      <PublicPagePreview business={business} onInquiry={onInquiry} />
    </section>
  );
}

function PublicPagePreview({ business, onInquiry }) {
  const [form, setForm] = useState(defaultInquiryForm(business));

  useEffect(() => {
    setForm(defaultInquiryForm(business));
  }, [business.id]);

  function submit(event) {
    event.preventDefault();
    if (!form.name || !form.phone) return;
    const selectedItem = business.catalogue.items.find((item) => String(item.id) === String(form.catalogueItemId));
    onInquiry({
      ...form,
      service: selectedItem?.name || '',
      source: 'Public catalogue page',
      expectedAmount: parseAmount(selectedItem?.price),
    });
    setForm(defaultInquiryForm(business));
  }

  return (
    <section className="public-layout">
      <div className="public-page full">
        <div className="public-hero">
          <p>{business.catalogue.audience}</p>
          <h1>{business.catalogue.headline}</h1>
          <span>{business.catalogue.subtext}</span>
          <div className="public-actions">
            <a className="primary-button" href={whatsAppHref(business, `Hi, I am interested in ${business.catalogue.items[0]?.name}`)}>
              <Phone size={16} />
              {business.catalogue.cta}
            </a>
            <button className="ghost-button" onClick={() => navigator.clipboard?.writeText(publicUrl(business))}>
              <Share2 size={16} />
              Share
            </button>
          </div>
        </div>

        <div className="service-grid">
          {business.catalogue.items.map((item) => (
            <article className="service-card" key={item.id}>
              <span>{item.format}</span>
              <h3>{item.name}</h3>
              <p>{item.description}</p>
              <small>{item.details}</small>
              <span>{item.timingOrTimeline}</span>
              <span>{item.terms}</span>
              <strong>{item.price}</strong>
            </article>
          ))}
        </div>

        {business.mediaAssets.length > 0 && (
          <div className="media-grid">
            {business.mediaAssets.map((asset) => (
              <figure className="media-card" key={asset.title}>
                <div style={{ background: asset.placeholderColor }} />
                <figcaption>
                  <strong>{asset.title}</strong>
                  <span>{asset.caption}</span>
                </figcaption>
              </figure>
            ))}
          </div>
        )}

        {business.caseStudies.length > 0 && (
          <div className="case-grid">
            {business.caseStudies.map((item) => (
              <article className="case-card" key={item.title}>
                <span>{item.clientContext}</span>
                <h3>{item.title}</h3>
                <p>{item.problem}</p>
                <strong>{item.outcome}</strong>
              </article>
            ))}
          </div>
        )}

        <div className="proof-strip">
          {business.proof.map((proof) => (
            <div key={proof}>
              <BadgeCheck size={18} />
              <strong>{proof}</strong>
            </div>
          ))}
        </div>

        <div className="testimonial-grid">
          {business.testimonials.map((testimonial) => (
            <blockquote key={testimonial.customerName}>
              <p>{testimonial.quote}</p>
              <footer>
                {testimonial.customerName} · {testimonial.customerContext}
              </footer>
            </blockquote>
          ))}
        </div>

        <div className="faq-grid">
          {business.catalogue.faqs.map((faq) => (
            <article key={faq.question}>
              <strong>{faq.question}</strong>
              <p>{faq.answer}</p>
            </article>
          ))}
        </div>
      </div>

      <form className="inquiry-form" onSubmit={submit}>
        <p className="eyebrow">Lead capture</p>
        <h2>{inquiryTitle(business.pack)}</h2>
        <label>
          Name
          <input value={form.name} onChange={(event) => setForm({ ...form, name: event.target.value })} />
        </label>
        <label>
          Phone
          <input value={form.phone} onChange={(event) => setForm({ ...form, phone: event.target.value })} />
        </label>
        <label>
          Interested service
          <select value={form.catalogueItemId} onChange={(event) => setForm({ ...form, catalogueItemId: event.target.value })}>
            {business.catalogue.items.map((item) => (
              <option value={item.id} key={item.id}>
                {item.name}
              </option>
            ))}
          </select>
        </label>
        {personaFormFields(business.pack).map((field) => (
          <label key={field.key}>
            {field.label}
            <input value={form[field.key]} onChange={(event) => setForm({ ...form, [field.key]: event.target.value })} />
          </label>
        ))}
        <label>
          Message
          <textarea value={form.note} onChange={(event) => setForm({ ...form, note: event.target.value })} />
        </label>
        <button className="primary-button" type="submit">
          <Plus size={16} />
          Create lead
        </button>
        <span className="form-note">BizzNexx creates a lead, suggests the next WhatsApp reply, and adds follow-up to the owner dashboard.</span>
      </form>
    </section>
  );
}

function MessagesView({ business }) {
  return (
    <section className="page-stack">
      <SectionTitle eyebrow="Messages" title="Templates should feel specific, not generic" />
      <div className="message-grid">
        {Object.entries(personaPacks[business.pack]?.messages || {}).map(([type, body]) => (
          <article className="message-card" key={type}>
            <span>{titleize(type)}</span>
            <p>{body}</p>
          </article>
        ))}
      </div>
    </section>
  );
}

function InsightsView({ business }) {
  const stats = getStats(business);
  return (
    <section className="page-stack">
      <SectionTitle eyebrow="Insights" title="Scores must explain action, not decorate the dashboard" />
      <div className="metric-grid">
        <Metric icon={Gauge} label="Growth Score" value={`${business.growthScore}/100`} tone="green" />
        <Metric icon={CheckCircle2} label="Health Score" value={`${business.healthScore}/100`} tone="blue" />
        <Metric icon={Eye} label="Proof assets" value={business.mediaAssets.length + business.caseStudies.length} tone="yellow" />
        <Metric icon={CreditCard} label="Pending" value={`Rs. ${stats.pendingAmount.toLocaleString('en-IN')}`} tone="rose" />
      </div>
      <Panel title="Score reasons">
        <div className="reason-grid">
          {business.scoreReasons.map((reason) => (
            <article className={`reason-card ${reason.severity}`} key={reason.label}>
              <strong>{reason.label}</strong>
              <span>{reason.detail}</span>
            </article>
          ))}
        </div>
      </Panel>
    </section>
  );
}

function OperatorSetup({ business, businesses, apiMode, refreshBusinesses, updateBusiness }) {
  async function updateStage(stage) {
    if (apiMode === 'api' && business.setupProjectId) {
      await api.updateSetupProject(business.setupProjectId, { stage: stage.toLowerCase().replaceAll(' ', '_') });
      await refreshBusinesses(business.id);
      return;
    }
    updateBusiness({ ...business, setupStage: stage });
  }

  return (
    <section className="page-stack">
      <SectionTitle eyebrow="Internal operator mode" title="Assisted setup quality control" />
      <div className="metric-grid">
        <Metric icon={Globe2} label="Businesses" value={businesses.length} tone="green" />
        <Metric icon={ClipboardList} label="Published" value={businesses.filter((item) => item.setupStage === 'Published').length} tone="blue" />
        <Metric icon={Users} label="Leads" value={businesses.reduce((sum, item) => sum + item.leads.length, 0)} tone="yellow" />
        <Metric icon={CreditCard} label="Open dues" value={`Rs. ${businesses.reduce((sum, item) => sum + getStats(item).pendingAmount, 0).toLocaleString('en-IN')}`} tone="rose" />
      </div>
      <div className="two-column">
        <Panel title="Setup stage">
          <div className="stage-list">
            {['Intake', 'Catalogue Draft', 'Page Review', 'Published', 'Weekly Review'].map((stage) => (
              <button key={stage} className={business.setupStage === stage ? 'stage active' : 'stage'} onClick={() => updateStage(stage)}>
                {stage}
              </button>
            ))}
          </div>
        </Panel>
        <Panel title="Quality checklist">
          <Checklist
            items={[
              ['Persona pack', personaPacks[business.pack]?.label],
              ['Services/packages', `${business.catalogue.items.length} items`],
              ['FAQs', `${business.catalogue.faqs.length} items`],
              ['Testimonials', `${business.testimonials.length} items`],
              ['Proof assets', `${business.mediaAssets.length + business.caseStudies.length} items`],
              ['Leads captured', `${business.leads.length} leads`],
            ]}
          />
        </Panel>
      </div>
      <Panel title="Notes and blockers">
        <div className="mobile-list">
          {business.operatorNotes.map((note) => (
            <article className={note.isBlocker ? 'note-card blocker' : 'note-card'} key={note.body}>
              <strong>{note.isBlocker ? 'Blocker' : 'Note'}</strong>
              <span>{note.body}</span>
            </article>
          ))}
        </div>
      </Panel>
    </section>
  );
}

function LeadActionList({ business, leads, apiMode, refreshBusinesses, updateBusiness, onDraft }) {
  const pack = personaPacks[business.pack] || personaPacks.tutor;

  async function updateLeadStatus(leadId, status) {
    if (apiMode === 'api') {
      await api.updateLeadStatus(leadId, { status });
      await refreshBusinesses(business.id);
      return;
    }
    updateBusiness({
      ...business,
      leads: business.leads.map((lead) => (lead.id === leadId ? { ...lead, status } : lead)),
    });
  }

  return (
    <div className="mobile-list">
      {leads.map((lead) => (
        <article className="mobile-card" key={lead.id}>
          <div>
            <strong>{lead.name}</strong>
            <span>
              {lead.service} · {lead.source}
            </span>
            <p>{lead.nextAction}</p>
            <small>{lead.urgencyReason || `${lead.followUpAgeDays || 0} day follow-up age`}</small>
          </div>
          <div className="inline-actions">
            <select value={lead.status} onChange={(event) => updateLeadStatus(lead.id, event.target.value)}>
              {pack.statuses.map((status) => (
                <option key={status}>{status}</option>
              ))}
            </select>
            <button
              className="icon-button"
              onClick={() =>
                onDraft({
                  title: `Follow up with ${lead.name}`,
                  body: fillTemplate(pack.messages.followUp, lead),
                })
              }
            >
              <Send size={16} />
            </button>
          </div>
        </article>
      ))}
    </div>
  );
}

function PaymentActionList({ business, payments, apiMode, refreshBusinesses, updateBusiness, onDraft }) {
  const pack = personaPacks[business.pack] || personaPacks.tutor;

  async function markPaid(paymentId) {
    if (apiMode === 'api') {
      await api.markPaymentPaid(paymentId);
      await refreshBusinesses(business.id);
      return;
    }
    updateBusiness({
      ...business,
      payments: business.payments.map((payment) => (payment.id === paymentId ? { ...payment, status: 'Paid' } : payment)),
    });
  }

  return (
    <div className="mobile-list">
      {payments.map((payment) => (
        <article className="mobile-card" key={payment.id}>
          <div>
            <strong>{payment.name}</strong>
            <span>{payment.service}</span>
            <p>
              Rs. {payment.amount.toLocaleString('en-IN')} · {payment.status}
            </p>
            <small>{payment.urgencyReason || `${payment.ageDays || 0} day payment age`}</small>
          </div>
          <div className="inline-actions">
            <button className="ghost-button compact" onClick={() => markPaid(payment.id)}>
              Paid
            </button>
            <button
              className="icon-button"
              onClick={() =>
                onDraft({
                  title: `Payment reminder for ${payment.name}`,
                  body: fillTemplate(pack.messages.payment, payment),
                })
              }
            >
              <MessageCircle size={16} />
            </button>
          </div>
        </article>
      ))}
    </div>
  );
}

function MessagePreview({ business, draft, onClose }) {
  const [body, setBody] = useState(draft.body);

  useEffect(() => {
    setBody(draft.body);
  }, [draft.body]);

  return (
    <div className="modal-backdrop">
      <section className="message-modal">
        <p className="eyebrow">Preview before WhatsApp</p>
        <h2>{draft.title}</h2>
        <textarea value={body} onChange={(event) => setBody(event.target.value)} />
        <div className="header-actions">
          <button className="ghost-button" onClick={onClose}>
            Close
          </button>
          <a className="primary-button" href={whatsAppHref(business, body)}>
            <MessageCircle size={16} />
            Open WhatsApp
          </a>
        </div>
      </section>
    </div>
  );
}

function Metric({ icon: Icon, label, value, tone }) {
  return (
    <div className={`metric-card ${tone}`}>
      <Icon size={20} />
      <span>{label}</span>
      <strong>{value}</strong>
    </div>
  );
}

function Panel({ title, children }) {
  return (
    <section className="panel">
      <h2>{title}</h2>
      {children}
    </section>
  );
}

function SectionTitle({ eyebrow, title }) {
  return (
    <header className="section-title">
      <p className="eyebrow">{eyebrow}</p>
      <h2>{title}</h2>
    </header>
  );
}

function Checklist({ items }) {
  return (
    <div className="checklist">
      {items.map(([label, status]) => (
        <div key={label}>
          <CheckCircle2 size={16} />
          <span>{label}</span>
          <strong>{status}</strong>
        </div>
      ))}
    </div>
  );
}

function loadBusinesses() {
  try {
    const saved = localStorage.getItem(STORAGE_KEY);
    const records = saved ? JSON.parse(saved) : starterBusinesses;
    return records.map(ensureBusinessDefaults);
  } catch {
    return starterBusinesses.map(ensureBusinessDefaults);
  }
}

function normalizeBusiness(record) {
  const catalogue = record.catalogue || { items: [], faqs: [] };
  return ensureBusinessDefaults({
    id: record.id,
    slug: record.public_slug,
    pack: record.persona_pack,
    name: record.name,
    owner: record.owner_name,
    city: record.city,
    whatsapp: record.whatsapp_number,
    tone: record.brand_tone,
    setupProjectId: record.setup_project?.id,
    setupStage: titleize(record.setup_project?.stage || 'published'),
    growthScore: record.growth_score,
    healthScore: record.health_score,
    catalogue: {
      audience: catalogue.audience || '',
      headline: catalogue.headline || '',
      subtext: catalogue.subtext || '',
      cta: catalogue.primary_cta || 'Contact',
      items: (catalogue.items || []).map((item) => ({
        id: item.id,
        name: item.name,
        format: item.format,
        price: item.price_label,
        description: item.description,
        details: item.details,
        timingOrTimeline: item.timing_or_timeline,
        terms: item.terms,
      })),
      faqs: (catalogue.faqs || []).map((faq) => ({
        question: faq.question,
        answer: faq.answer,
      })),
    },
    proof: (record.trust_proof || []).map((proof) => proof.title),
    mediaAssets: (record.media_assets || []).map((asset) => ({
      title: asset.title,
      category: asset.category,
      placeholderColor: asset.placeholder_color,
      caption: asset.caption,
    })),
    testimonials: (record.testimonials || []).map((testimonial) => ({
      customerName: testimonial.customer_name,
      customerContext: testimonial.customer_context,
      quote: testimonial.quote,
    })),
    caseStudies: (record.case_studies || []).map((item) => ({
      title: item.title,
      clientContext: item.client_context,
      problem: item.problem,
      workDone: item.work_done,
      outcome: item.outcome,
    })),
    leads: (record.leads || []).map((lead) => ({
      id: lead.id,
      name: lead.name,
      phone: lead.phone_number,
      service: lead.interested_service,
      source: lead.source,
      status: lead.status,
      nextAction: lead.next_action,
      amount: Number(lead.expected_value || 0),
      followUpAgeDays: lead.follow_up_age_days,
      urgencyReason: lead.urgency_reason,
    })),
    payments: (record.payments || []).map((payment) => ({
      id: payment.id,
      name: payment.payer_name,
      service: payment.service_name,
      amount: Number(payment.amount_due || 0),
      status: titleize(payment.status),
      ageDays: payment.age_days,
      urgencyReason: payment.urgency_reason,
    })),
    scoreReasons: (record.score_reasons || []).map((reason) => ({
      label: reason.label,
      detail: reason.detail,
      severity: reason.severity,
    })),
    operatorNotes: (record.operator_notes || []).map((note) => ({
      body: note.body,
      isBlocker: note.is_blocker,
    })),
  });
}

function ensureBusinessDefaults(business) {
  return {
    ...business,
    catalogue: {
      ...(business.catalogue || {}),
      items: business.catalogue?.items || [],
      faqs: business.catalogue?.faqs || [],
    },
    proof: business.proof || [],
    mediaAssets: business.mediaAssets || [],
    testimonials: business.testimonials || [],
    caseStudies: business.caseStudies || [],
    leads: (business.leads || []).map((lead) => ({
      followUpAgeDays: 0,
      urgencyReason: '',
      ...lead,
    })),
    payments: (business.payments || []).map((payment) => ({
      ageDays: 0,
      urgencyReason: '',
      ...payment,
    })),
    scoreReasons: business.scoreReasons || [],
    operatorNotes: business.operatorNotes || [],
  };
}

function getStats(business) {
  const pendingPayments = business.payments.filter((payment) => payment.status !== 'Paid');
  return {
    openLeads: business.leads.filter((lead) => !['Enrolled', 'Booked', 'Won', 'Lost'].includes(lead.status)).length,
    followUps: business.leads.filter((lead) => lead.nextAction).length,
    pendingAmount: pendingPayments.reduce((sum, payment) => sum + payment.amount, 0),
  };
}

function defaultInquiryForm(business) {
  return {
    name: '',
    phone: '',
    catalogueItemId: business.catalogue.items[0]?.id || '',
    note: '',
    detailOne: '',
    detailTwo: '',
  };
}

function personaFormFields(pack) {
  if (pack === 'tutor') {
    return [
      { key: 'detailOne', label: 'Class / Board' },
      { key: 'detailTwo', label: 'Preferred timing' },
    ];
  }
  if (pack === 'event') {
    return [
      { key: 'detailOne', label: 'Event date' },
      { key: 'detailTwo', label: 'Venue / Location' },
    ];
  }
  return [
    { key: 'detailOne', label: 'Budget range' },
    { key: 'detailTwo', label: 'Timeline' },
  ];
}

function inquiryTitle(pack) {
  if (pack === 'event') return 'Check availability';
  if (pack === 'agency') return 'Request discovery call';
  return 'Book trial / ask details';
}

function fillTemplate(template, entity) {
  return String(template || '')
    .replace('{name}', entity.name || '')
    .replace('{service}', entity.service || '')
    .replace('{amount}', entity.amount?.toLocaleString('en-IN') || '');
}

function whatsAppHref(business, text) {
  return `https://wa.me/${business.whatsapp}?text=${encodeURIComponent(text)}`;
}

function publicUrl(business) {
  return `${window.location.origin}/b/${business.slug}`;
}

function parseAmount(price) {
  const match = String(price || '').replace(/,/g, '').match(/\d+/);
  return match ? Number(match[0]) : 0;
}

function titleize(value) {
  return String(value || '')
    .replaceAll('_', ' ')
    .replace(/\b\w/g, (char) => char.toUpperCase());
}

function coerceId(value) {
  const numeric = Number(value);
  return Number.isNaN(numeric) ? value : numeric;
}

createRoot(document.getElementById('root')).render(<App />);
