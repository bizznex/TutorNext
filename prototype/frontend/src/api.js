const API_BASE = import.meta.env.VITE_API_BASE || 'http://localhost:8000/api';

async function request(path, options = {}) {
  const response = await fetch(`${API_BASE}${path}`, {
    headers: {
      'Content-Type': 'application/json',
      ...(options.headers || {}),
    },
    ...options,
  });
  if (!response.ok) {
    const body = await response.text();
    throw new Error(body || `Request failed: ${response.status}`);
  }
  return response.json();
}

export const api = {
  getBusinesses: () => request('/businesses/'),
  getSummary: (businessId) => request(`/businesses/${businessId}/summary/`),
  captureInquiry: (payload) =>
    request('/inquiries/capture/', {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
  updateLeadStatus: (leadId, payload) =>
    request(`/leads/${leadId}/set_status/`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
  getLeadMessage: (leadId) => request(`/leads/${leadId}/suggested_message/`),
  markPaymentPaid: (paymentId, payload = {}) =>
    request(`/payments/${paymentId}/mark_paid/`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
  getPaymentReminder: (paymentId) => request(`/payments/${paymentId}/reminder/`),
  updateSetupProject: (setupId, payload) =>
    request(`/setup-projects/${setupId}/`, {
      method: 'PATCH',
      body: JSON.stringify(payload),
    }),
  logPageEvent: (businessId, payload) =>
    request(`/businesses/${businessId}/page_event/`, {
      method: 'POST',
      body: JSON.stringify(payload),
    }),
};
