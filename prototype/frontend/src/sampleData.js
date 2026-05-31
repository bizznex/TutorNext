export const personaPacks = {
  tutor: {
    label: 'Tutor / Coach',
    statuses: ['New inquiry', 'Contacted', 'Trial scheduled', 'Fee sent', 'Enrolled', 'Lost'],
    inquiryFields: ['studentClass', 'preferredTime'],
    messages: {
      firstReply:
        'Hi {name}, thanks for your inquiry. I can help with {service}. Would you like to book a trial class this week?',
      followUp:
        'Hi {name}, gentle follow-up on your interest in {service}. Should I reserve a trial slot for you?',
      payment:
        'Hi {name}, gentle reminder that Rs. {amount} is pending for {service}. Please share confirmation once paid.',
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
      audience: 'For Class 8-12 students and parents',
      headline: 'Maths and Science coaching with trial classes and monthly parent updates.',
      subtext:
        'Online and offline batches for CBSE, ICSE, and WB board students. Book a trial before joining.',
      cta: 'Book trial class',
      items: [
        {
          id: 'svc_math',
          name: 'Class 9-10 Maths Foundation',
          format: 'Group batch',
          price: 'Rs. 2,500/month',
          description: 'Concept building, weekly practice, and parent progress updates.',
        },
        {
          id: 'svc_physics',
          name: 'Class 11-12 Physics Support',
          format: 'Small group',
          price: 'Rs. 3,500/month',
          description: 'Numericals, board preparation, doubt clearing, and revision plans.',
        },
        {
          id: 'svc_doubt',
          name: 'One-to-One Doubt Class',
          format: '1:1 session',
          price: 'Rs. 800/session',
          description: 'Focused support for weak chapters before exams or tests.',
        },
      ],
      faqs: ['Do you offer trial classes?', 'Are classes online or offline?', 'How are parents updated?'],
    },
    proof: [
      '8 years teaching experience',
      '120+ students taught',
      'Monthly parent progress notes',
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
      },
    ],
    payments: [
      { id: 'pay_1', name: 'Aarav', service: 'Class 9 Maths', amount: 2500, status: 'Overdue' },
      { id: 'pay_2', name: 'Sohini', service: 'Doubt Class', amount: 1600, status: 'Part paid' },
      { id: 'pay_3', name: 'Naina', service: 'Maths Foundation', amount: 2500, status: 'Paid' },
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
