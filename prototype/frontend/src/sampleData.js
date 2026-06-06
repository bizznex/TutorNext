export const personaPacks = {
  tutor: {
    label: 'Tutor / Coach',
    statuses: ['New inquiry', 'Trial options sent', 'Trial scheduled', 'Trial completed', 'Fee plan sent', 'Enrolled', 'Lost'],
    inquiryFields: ['studentClass', 'preferredTime'],
    messages: {
      firstReply:
        'Hi {name}, thanks for your inquiry. I can help with {service}. Please share the student class/board and preferred timing, and I will suggest a trial slot.',
      followUp:
        'Hi {name}, gentle follow-up on your interest in {service}. Would you like me to reserve a trial slot this week?',
      payment:
        'Hi {name}, gentle reminder that Rs. {amount} is pending for {service}. Please share confirmation once paid. Thank you.',
    },
  },
  event: {
    label: 'Event Service',
    statuses: ['New event inquiry', 'Availability checked', 'Package shared', 'Advance pending', 'Booked', 'Lost'],
    inquiryFields: ['eventDate', 'location'],
    messages: {
      firstReply:
        'Hi {name}, thanks for reaching out. Please share your event date and location so I can confirm availability for {service}.',
      followUp:
        'Hi {name}, following up on the {service} package. I can block the date once the advance is confirmed.',
      payment:
        'Hi {name}, gentle reminder that Rs. {amount} is pending for {service}. Please share confirmation after payment.',
    },
  },
  agency: {
    label: 'Freelancer / Agency',
    statuses: ['New inquiry', 'Discovery booked', 'Proposal sent', 'Follow-up due', 'Won', 'Lost'],
    inquiryFields: ['budgetRange', 'projectType'],
    messages: {
      firstReply:
        'Hi {name}, thanks for your inquiry. I can help with {service}. Would you like to schedule a short discovery call?',
      followUp:
        'Hi {name}, checking in on the proposal for {service}. Happy to clarify scope, timeline, or pricing.',
      payment:
        'Hi {name}, gentle reminder that Rs. {amount} is pending for the {service} milestone.',
    },
  },
};

export const starterBusinesses = [
  {
    id: 'biz_tutor_1',
    slug: 'ananya-learning-studio',
    pack: 'tutor',
    name: 'Ananya Learning Studio',
    owner: 'Ananya Sharma',
    city: 'Kolkata',
    whatsapp: '919876543210',
    tone: 'Friendly Hinglish',
    setupStage: 'Published',
    growthScore: 74,
    healthScore: 68,
    catalogue: {
      audience: 'For Class 8-12 students and parents in South Kolkata',
      headline: 'Maths and Science support for Classes 8-12, with trial assessment and parent updates.',
      subtext:
        'Hybrid CBSE, ICSE, and WB board batches with structured revision, patient doubt clearing, and clear monthly fee reminders.',
      cta: 'Book trial class',
      items: [
        {
          id: 'svc_math',
          name: 'Class 9-10 Maths Foundation',
          format: 'Group batch',
          price: 'Rs. 2,500/month',
          description: 'Concept building, weekly practice, board-style sums, and revision support before school tests.',
          details: 'Best for students who need stronger fundamentals before board-prep years.',
          timingOrTimeline: 'Tue/Thu 6 PM, Sat 11 AM',
          terms: 'Free 30-minute assessment before joining',
        },
        {
          id: 'svc_physics',
          name: 'Class 11-12 Physics Support',
          format: 'Small group',
          price: 'Rs. 3,500/month',
          description: 'Numericals, board preparation, doubt clearing, and chapter-wise revision plans.',
          details: 'Designed for students who need personal attention beyond large coaching classes.',
          timingOrTimeline: 'Mon/Wed 7 PM',
          terms: 'Rs. 300 trial session',
        },
        {
          id: 'svc_doubt',
          name: 'One-to-One Doubt Class',
          format: '1:1 session',
          price: 'Rs. 800/session',
          description: 'Focused support for weak chapters, upcoming tests, or exam-week confusion.',
          details: 'Parents can request a specific chapter or worksheet before the session.',
          timingOrTimeline: 'Slots shared based on weekly availability',
          terms: 'Pay per session',
        },
      ],
      faqs: [
        {
          question: 'Do you offer trial classes?',
          answer: 'Yes. Class 9-10 students can take a free 30-minute assessment. Class 11-12 Physics has a paid trial session.',
        },
        {
          question: 'Which boards do you support?',
          answer: 'CBSE, ICSE, and WB board students are supported. The inquiry form asks for class and board so the right batch can be suggested.',
        },
        {
          question: 'How are parents updated?',
          answer: 'Parents receive simple monthly progress notes and reminders for fees, trials, and revision plans.',
        },
        {
          question: 'Can fees be discussed privately?',
          answer: 'Yes. Fees can be shown publicly, shared as a range, or discussed after the first trial depending on the tutor preference.',
        },
      ],
    },
    proof: [
      '8 years Maths and Science teaching experience',
      '120+ students taught',
      '2025 batch: 14 students scored 80+ in Maths/Science',
      'Monthly parent progress notes and fee reminders',
    ],
    testimonials: [
      {
        customerName: 'Parent of Class 10 ICSE student',
        customerContext: 'Maths Foundation',
        quote: 'My son became more confident before boards because concepts were explained patiently and revision was structured.',
      },
      {
        customerName: 'Parent of Class 12 CBSE student',
        customerContext: 'Physics Support',
        quote: 'The small batch helped with numericals and doubts. We also got timely updates before tests.',
      },
    ],
    leads: [
      {
        id: 'lead_1',
        name: 'Rohit parent',
        phone: '9830001111',
        service: 'Class 9-10 Maths Foundation',
        source: 'Catalogue page',
        status: 'New inquiry',
        nextAction: 'Send first response and trial class options',
        amount: 2500,
        followUpAgeDays: 1,
        urgencyReason: 'Class 10 ICSE parent asked for trial options yesterday.',
      },
      {
        id: 'lead_2',
        name: 'Meera parent',
        phone: '9830002222',
        service: 'Class 11-12 Physics Support',
        source: 'Instagram bio',
        status: 'Trial scheduled',
        nextAction: 'Send trial reminder at 4 PM',
        amount: 3500,
        followUpAgeDays: 0,
        urgencyReason: 'Trial is due today. Reminder should go before the 7 PM session.',
      },
      {
        id: 'lead_5',
        name: 'Ayan parent',
        phone: '9830003333',
        service: 'Class 9-10 Maths Foundation',
        source: 'WhatsApp referral',
        status: 'Trial options sent',
        nextAction: 'Follow up after parent asked for fee details',
        amount: 2500,
        followUpAgeDays: 3,
        urgencyReason: 'Parent has fee details but no trial slot is confirmed yet.',
      },
    ],
    payments: [
      {
        id: 'pay_1',
        name: 'Aarav',
        service: 'Class 9 Maths',
        amount: 2500,
        status: 'Overdue',
        ageDays: 6,
        urgencyReason: 'Monthly fee is 6 days overdue. Send a polite UPI reminder.',
      },
      {
        id: 'pay_2',
        name: 'Sohini',
        service: 'Doubt Class',
        amount: 1600,
        status: 'Part paid',
        ageDays: 2,
        urgencyReason: 'Rs. 800 paid, balance is still pending after the second doubt class.',
      },
      { id: 'pay_3', name: 'Naina', service: 'Maths Foundation', amount: 2500, status: 'Paid', ageDays: 0 },
    ],
  },
  {
    id: 'biz_event_1',
    slug: 'ria-bridal-studio',
    pack: 'event',
    name: 'Ria Bridal Studio',
    owner: 'Ria Das',
    city: 'Durgapur',
    whatsapp: '919811223344',
    tone: 'Warm professional',
    setupStage: 'Page review',
    growthScore: 69,
    healthScore: 61,
    catalogue: {
      audience: 'For brides, families, and event bookings',
      headline: 'Bridal makeup, party looks, and event styling with clear packages.',
      subtext:
        'Share your event date and preferred look. We confirm availability, package, advance, and balance clearly.',
      cta: 'Check availability',
      items: [
        {
          id: 'svc_bridal',
          name: 'Bridal Makeup Package',
          format: 'Wedding day',
          price: 'Starting Rs. 12,000',
          description: 'HD bridal makeup, hair styling, draping, and pre-event consultation.',
        },
        {
          id: 'svc_party',
          name: 'Party Makeup',
          format: 'Single session',
          price: 'Starting Rs. 3,500',
          description: 'Elegant party-ready makeup for receptions, birthdays, and family events.',
        },
        {
          id: 'svc_engagement',
          name: 'Engagement Look',
          format: 'Event package',
          price: 'Starting Rs. 7,000',
          description: 'Soft glam or traditional look with hair styling and consultation.',
        },
      ],
      faqs: ['How much advance is required?', 'Do you travel to venue?', 'Can I see previous looks?'],
    },
    proof: ['45+ bridal looks', 'Venue service available', 'Advance locks date'],
    leads: [
      {
        id: 'lead_3',
        name: 'Priyanka',
        phone: '9900001111',
        service: 'Bridal Makeup Package',
        source: 'Instagram',
        status: 'Package shared',
        nextAction: 'Confirm event date and advance',
        amount: 12000,
      },
    ],
    payments: [
      { id: 'pay_4', name: 'Priyanka', service: 'Bridal Package Advance', amount: 4000, status: 'Unpaid' },
    ],
  },
  {
    id: 'biz_agency_1',
    slug: 'northstar-design-co',
    pack: 'agency',
    name: 'Northstar Design Co.',
    owner: 'Arjun Mehta',
    city: 'Bengaluru',
    whatsapp: '919900112233',
    tone: 'Sharp professional',
    setupStage: 'Draft',
    growthScore: 63,
    healthScore: 59,
    catalogue: {
      audience: 'For founders and small teams',
      headline: 'Brand, website, and content design for growing small businesses.',
      subtext:
        'Turn unclear ideas into clean launch-ready assets. Start with a discovery call.',
      cta: 'Book discovery call',
      items: [
        {
          id: 'svc_brand',
          name: 'Starter Brand Kit',
          format: 'Fixed package',
          price: 'Starting Rs. 18,000',
          description: 'Logo direction, color system, typography, and launch-ready brand basics.',
        },
        {
          id: 'svc_landing',
          name: 'Landing Page Design',
          format: 'Project',
          price: 'Starting Rs. 25,000',
          description: 'Conversion-focused page structure, copy guidance, and responsive design.',
        },
        {
          id: 'svc_content',
          name: 'Content Design Retainer',
          format: 'Monthly',
          price: 'Starting Rs. 15,000/month',
          description: 'Social and marketing design support for recurring campaigns.',
        },
      ],
      faqs: ['Do you handle development?', 'How long does delivery take?', 'Do you offer retainers?'],
    },
    proof: ['12 launch projects', 'Founder-friendly process', 'Milestone billing'],
    leads: [
      {
        id: 'lead_4',
        name: 'Kavya Foods',
        phone: '9876501234',
        service: 'Landing Page Design',
        source: 'Referral',
        status: 'Proposal sent',
        nextAction: 'Follow up on proposal by evening',
        amount: 25000,
      },
    ],
    payments: [
      { id: 'pay_5', name: 'Kavya Foods', service: 'Landing Page Milestone', amount: 10000, status: 'Part paid' },
    ],
  },
];
