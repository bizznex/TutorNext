from django.core.management.base import BaseCommand

from businesses.models import (
    Business,
    Catalogue,
    CatalogueItem,
    CaseStudy,
    FAQ,
    Lead,
    MediaAsset,
    MessageTemplate,
    OperatorNote,
    Payment,
    ScoreReason,
    SetupProject,
    Testimonial,
    TrustProof,
)
from businesses.personas import PERSONA_PACKS


class Command(BaseCommand):
    help = "Seed realistic BizzNexx pilot data."

    def handle(self, *args, **options):
        Business.objects.all().delete()

        self.seed_tutor()
        self.seed_bridal()
        self.seed_agency()

        self.stdout.write(self.style.SUCCESS("Seeded realistic BizzNexx pilot data."))

    def create_messages(self, business):
        for message_type, body in PERSONA_PACKS[business.persona_pack]["messages"].items():
            MessageTemplate.objects.create(
                business=business,
                message_type=message_type,
                body=body,
                tone=business.brand_tone,
                language=business.preferred_language,
            )

    def seed_tutor(self):
        business = Business.objects.create(
            name="Ananya Learning Studio",
            owner_name="Ananya Sharma",
            persona_pack="tutor",
            city="Kolkata",
            whatsapp_number="919876543210",
            public_slug="ananya-learning-studio",
            preferred_language="English + Hinglish",
            brand_tone="Calm, parent-friendly",
            payment_terms="Monthly UPI before the 7th; part-payment allowed only after discussion.",
            growth_score=76,
            health_score=64,
        )
        SetupProject.objects.create(
            business=business,
            stage=SetupProject.Stage.PUBLISHED,
            owner_inputs_complete=True,
        )
        catalogue = Catalogue.objects.create(
            business=business,
            audience="For Class 8-12 students and parents in South Kolkata",
            headline="Maths and Science support for Classes 8-12, with trial assessment and parent updates.",
            subtext="Hybrid CBSE, ICSE, and WB board batches with structured revision, patient doubt clearing, and clear monthly fee reminders.",
            primary_cta="Book a trial class",
            is_published=True,
        )
        items = [
            (
                "Class 9-10 Maths Foundation",
                "Group batch",
                "Concept building, weekly practice, board-style sums, and revision support before school tests.",
                "Rs. 2,500/month",
                "Best for students who need stronger fundamentals before board-prep years.",
                "Tue/Thu 6 PM, Sat 11 AM",
                "Free 30-minute assessment before joining",
            ),
            (
                "Class 11-12 Physics Support",
                "Small group",
                "Numericals, board preparation, doubt clearing, and chapter-wise revision plans.",
                "Rs. 3,500/month",
                "Designed for students who need personal attention beyond large coaching classes.",
                "Mon/Wed 7 PM",
                "Rs. 300 trial session",
            ),
            (
                "One-to-One Doubt Class",
                "1:1 session",
                "Focused support for weak chapters, upcoming tests, or exam-week confusion.",
                "Rs. 800/session",
                "Parents can request a specific chapter or worksheet before the session.",
                "Slots shared based on weekly availability",
                "Pay per session",
            ),
        ]
        for index, item in enumerate(items):
            CatalogueItem.objects.create(
                catalogue=catalogue,
                name=item[0],
                format=item[1],
                description=item[2],
                price_label=item[3],
                details=item[4],
                timing_or_timeline=item[5],
                terms=item[6],
                display_order=index,
            )
        for index, qa in enumerate(
            [
                ("Do you offer trial classes?", "Yes. Class 9-10 students can take a free 30-minute assessment. Class 11-12 Physics has a paid trial session."),
                ("Which boards do you support?", "CBSE, ICSE, and WB board students are supported. The inquiry form asks for class and board so the right batch can be suggested."),
                ("How are parents updated?", "Parents receive simple monthly progress notes and reminders for fees, trials, and revision plans."),
                ("Can fees be discussed privately?", "Yes. Fees can be shown publicly, shared as a range, or discussed after the first trial depending on the tutor preference."),
            ]
        ):
            FAQ.objects.create(catalogue=catalogue, question=qa[0], answer=qa[1], display_order=index)
        for proof in [
            "8 years Maths and Science teaching experience",
            "120+ students taught",
            "2025 batch: 14 students scored 80+ in Maths/Science",
            "Monthly parent progress notes and fee reminders",
        ]:
            TrustProof.objects.create(business=business, title=proof)
        Testimonial.objects.create(
            business=business,
            customer_name="Parent of Class 10 ICSE student",
            customer_context="Maths Foundation",
            quote="My son became more confident before boards because concepts were explained patiently and revision was structured.",
        )
        Testimonial.objects.create(
            business=business,
            customer_name="Parent of Class 12 CBSE student",
            customer_context="Physics Support",
            quote="The small batch helped with numericals and doubts. We also got timely updates before tests.",
        )
        MediaAsset.objects.create(
            business=business,
            title="Revision worksheet preview",
            category="Teaching proof",
            placeholder_color="#d7eadf",
            caption="Weekly practice and revision structure",
        )
        Lead.objects.create(
            business=business,
            name="Rohit parent",
            phone_number="9830001111",
            interested_service="Class 9-10 Maths Foundation",
            source="Catalogue page",
            status="New inquiry",
            expected_value=2500,
            next_action="Send trial options and ask preferred timing",
            follow_up_age_days=1,
            urgency_reason="Class 10 ICSE parent asked for trial options yesterday.",
        )
        Lead.objects.create(
            business=business,
            name="Meera parent",
            phone_number="9830002222",
            interested_service="Class 11-12 Physics Support",
            source="Instagram bio",
            status="Trial scheduled",
            expected_value=3500,
            next_action="Send trial reminder before 7 PM session",
            follow_up_age_days=0,
            urgency_reason="Trial is due today. Reminder should go before the 7 PM session.",
        )
        Lead.objects.create(
            business=business,
            name="Ayan parent",
            phone_number="9830003333",
            interested_service="Class 9-10 Maths Foundation",
            source="WhatsApp referral",
            status="Trial options sent",
            expected_value=2500,
            next_action="Follow up after parent asked for fee details",
            follow_up_age_days=3,
            urgency_reason="Parent has fee details but no trial slot is confirmed yet.",
        )
        Payment.objects.create(
            business=business,
            payer_name="Aarav",
            service_name="Class 9 Maths",
            amount_due=2500,
            status="overdue",
            age_days=6,
            urgency_reason="Monthly fee is 6 days overdue. Send a polite UPI reminder.",
            payment_mode="UPI",
        )
        Payment.objects.create(
            business=business,
            payer_name="Sohini",
            service_name="One-to-One Doubt Class",
            amount_due=1600,
            amount_paid=800,
            status="part_paid",
            age_days=2,
            urgency_reason="Rs. 800 paid, balance is still pending after the second doubt class.",
            payment_mode="UPI",
        )
        ScoreReason.objects.create(
            business=business,
            score_type="health",
            label="Fee collection needs attention",
            detail="Rs. 3,300 is pending across 2 students.",
            severity="warning",
        )
        OperatorNote.objects.create(
            business=business,
            body="Need one more parent testimonial and exact batch capacity before paid pilot.",
            is_blocker=False,
        )
        self.create_messages(business)

    def seed_bridal(self):
        business = Business.objects.create(
            name="Ria Bridal Studio",
            owner_name="Ria Das",
            persona_pack="event",
            city="Durgapur",
            whatsapp_number="919811223344",
            public_slug="ria-bridal-studio",
            preferred_language="Bengali + Hindi + English",
            brand_tone="Warm, polished, reassuring",
            payment_terms="Advance blocks event date; balance due before or on event day.",
            growth_score=71,
            health_score=58,
        )
        SetupProject.objects.create(business=business, stage=SetupProject.Stage.PAGE_REVIEW, owner_inputs_complete=False)
        catalogue = Catalogue.objects.create(
            business=business,
            audience="For brides, families, and event bookings in Durgapur, Asansol, and Bardhaman",
            headline="Bridal, engagement, and party makeup with clear packages and date booking support.",
            subtext="Share your event date, venue, and preferred look. We confirm availability and package options before booking.",
            primary_cta="Check event availability",
            is_published=True,
        )
        items = [
            ("Bridal Makeup Package", "Wedding day", "HD makeup, hair styling, draping, and pre-event consultation.", "Starting Rs. 12,000", "For wedding day bridal look with venue service.", "Event date based", "Rs. 4,000 advance to block date"),
            ("Engagement Look", "Event package", "Soft glam or traditional look with hair styling and saree/dupatta setting.", "Starting Rs. 7,000", "For engagement, reception, or family ceremony.", "Event date based", "Rs. 2,500 advance"),
            ("Party Makeup", "Single session", "Elegant party-ready makeup for receptions, birthdays, and family events.", "Starting Rs. 3,500", "For lighter event looks.", "Event date based", "Rs. 1,000 advance"),
        ]
        for index, item in enumerate(items):
            CatalogueItem.objects.create(catalogue=catalogue, name=item[0], format=item[1], description=item[2], price_label=item[3], details=item[4], timing_or_timeline=item[5], terms=item[6], display_order=index)
        for index, qa in enumerate([
            ("How much advance is required?", "Advance depends on the package and blocks the date after confirmation."),
            ("Do you travel to venue?", "Yes, venue service is available in Durgapur, Asansol, Bardhaman, and nearby areas."),
            ("Can I see previous looks?", "Yes, portfolio samples are shared before package finalization."),
        ]):
            FAQ.objects.create(catalogue=catalogue, question=qa[0], answer=qa[1], display_order=index)
        for proof in ["45+ bridal looks", "Venue service available", "Advance locks event date"]:
            TrustProof.objects.create(business=business, title=proof)
        for index, title in enumerate(["Classic Bengali bridal look", "Soft engagement glam", "Reception party look", "Minimal day event look"]):
            MediaAsset.objects.create(business=business, title=title, category="Portfolio", placeholder_color=["#e7c5bc", "#d9b7c6", "#c9b7d9", "#e5d3bb"][index], caption="Synthetic portfolio placeholder", display_order=index)
        Testimonial.objects.create(business=business, customer_name="Priyanka S.", customer_context="Bridal client", quote="Makeup stayed fresh through the full ceremony and the booking process was clear.")
        Lead.objects.create(business=business, name="Priyanka", phone_number="9900001111", interested_service="Bridal Makeup Package", source="Instagram", status="Package shared", expected_value=12000, next_action="Ask for advance to block date", follow_up_age_days=1, urgency_reason="Event date can be lost if advance is delayed.")
        Lead.objects.create(business=business, name="Sanchita", phone_number="9900002222", interested_service="Engagement Look", source="Catalogue page", status="Availability checked", expected_value=7000, next_action="Send package comparison", follow_up_age_days=2, urgency_reason="Prospect asked for two package options.")
        Payment.objects.create(business=business, payer_name="Priyanka", service_name="Bridal Package Advance", amount_due=4000, status="unpaid", age_days=0, urgency_reason="Advance needed to block event date.", payment_mode="UPI")
        Payment.objects.create(business=business, payer_name="Mitali", service_name="Party Makeup Balance", amount_due=2500, status="overdue", age_days=2, urgency_reason="Balance pending after completed event.", payment_mode="UPI")
        ScoreReason.objects.create(business=business, score_type="growth", label="Portfolio is required", detail="Visual businesses need gallery proof before paid pilot.", severity="warning")
        OperatorNote.objects.create(business=business, body="Replace synthetic gallery placeholders with real bridal portfolio before external sharing.", is_blocker=True)
        self.create_messages(business)

    def seed_agency(self):
        business = Business.objects.create(
            name="Northstar Design Co.",
            owner_name="Arjun Mehta",
            persona_pack="agency",
            city="Bengaluru",
            whatsapp_number="919900112233",
            public_slug="northstar-design-co",
            preferred_language="English",
            brand_tone="Sharp, professional, founder-friendly",
            payment_terms="50% advance for fixed projects; milestone payment before final handover.",
            growth_score=67,
            health_score=60,
        )
        SetupProject.objects.create(business=business, stage=SetupProject.Stage.CATALOGUE_DRAFT, owner_inputs_complete=True)
        catalogue = Catalogue.objects.create(
            business=business,
            audience="For founders and small teams preparing to launch",
            headline="Brand and landing page design for founders who need to launch clearly and look credible.",
            subtext="We help early-stage businesses turn rough ideas into clean brand systems, landing pages, and campaign assets.",
            primary_cta="Book discovery call",
            is_published=True,
        )
        items = [
            ("Starter Brand Kit", "Fixed package", "Logo direction, colors, typography, and launch-ready brand basics.", "Starting Rs. 18,000", "Best for founders who need a clean identity before launch.", "7-10 days", "50% advance"),
            ("Landing Page Design", "Project", "Conversion-focused page structure, copy guidance, and responsive design.", "Starting Rs. 25,000", "Best for products and services preparing a campaign or waitlist.", "10-14 days", "Milestone billing"),
            ("Content Design Retainer", "Monthly", "Design support for recurring social and marketing campaigns.", "Starting Rs. 15,000/month", "Best for teams needing 10-12 creatives per month.", "Monthly", "Monthly advance"),
        ]
        for index, item in enumerate(items):
            CatalogueItem.objects.create(catalogue=catalogue, name=item[0], format=item[1], description=item[2], price_label=item[3], details=item[4], timing_or_timeline=item[5], terms=item[6], display_order=index)
        for index, qa in enumerate([
            ("Do you handle development?", "Development can be coordinated separately; this page focuses on design and launch assets."),
            ("How long does delivery take?", "Most starter projects take 7-14 days depending on scope clarity."),
            ("Do you offer retainers?", "Yes, monthly content design retainers are available for recurring campaigns."),
        ]):
            FAQ.objects.create(catalogue=catalogue, question=qa[0], answer=qa[1], display_order=index)
        for proof in ["12 launch projects", "Founder-friendly process", "Milestone billing"]:
            TrustProof.objects.create(business=business, title=proof)
        CaseStudy.objects.create(business=business, title="D2C snack brand launch page", client_context="Early-stage food brand", problem="The founder had a product but no clear launch story.", work_done="Created page structure, messaging blocks, and responsive landing design.", outcome="Founder used the page for first retailer and customer outreach.")
        CaseStudy.objects.create(business=business, title="SaaS waitlist page", client_context="B2B SaaS founder", problem="The product was technical and hard to explain.", work_done="Simplified positioning, designed hero, feature sections, and lead capture flow.", outcome="The team started collecting qualified discovery calls.")
        Testimonial.objects.create(business=business, customer_name="Founder, Kavya Foods", customer_context="Landing page client", quote="They helped us explain our product clearly before launch.")
        MediaAsset.objects.create(business=business, title="Landing page mockup", category="Work sample", placeholder_color="#bfd7ea", caption="Synthetic work sample placeholder")
        Lead.objects.create(business=business, name="Kavya Foods", phone_number="9876501234", interested_service="Landing Page Design", source="Referral", status="Proposal sent", expected_value=30000, next_action="Follow up on scope and timeline", follow_up_age_days=5, urgency_reason="Proposal has been open for 5 days.")
        Lead.objects.create(business=business, name="FinPilot", phone_number="9876505678", interested_service="Starter Brand Kit", source="LinkedIn", status="Discovery booked", expected_value=18000, next_action="Send pre-call questions", follow_up_age_days=0, urgency_reason="Discovery call booked for tomorrow.")
        Payment.objects.create(business=business, payer_name="Kavya Foods", service_name="Landing Page Milestone 1", amount_due=10000, amount_paid=5000, status="part_paid", age_days=5, urgency_reason="Milestone balance pending before next handover.", payment_mode="Bank transfer")
        ScoreReason.objects.create(business=business, score_type="growth", label="Case studies need stronger visuals", detail="Two case studies exist, but work samples are still placeholders.", severity="warning")
        OperatorNote.objects.create(business=business, body="Ask for real screenshots or approved portfolio visuals before founder feedback calls.", is_blocker=True)
        self.create_messages(business)
