PERSONA_PACKS = {
    "tutor": {
        "label": "Tutor / Coach",
        "statuses": ["New inquiry", "Contacted", "Trial scheduled", "Fee sent", "Enrolled", "Lost"],
        "first_status": "New inquiry",
        "first_action": "Send first response and offer trial options",
        "messages": {
            "first_reply": "Hi {name}, thanks for your inquiry. I can help with {service}. Would you like to book a trial class this week?",
            "follow_up": "Hi {name}, gentle follow-up on your interest in {service}. Should I reserve a trial slot for you?",
            "payment": "Hi {name}, gentle reminder that Rs. {amount} is pending for {service}. Please share confirmation once paid.",
        },
    },
    "event": {
        "label": "Event Service",
        "statuses": ["New event inquiry", "Availability checked", "Package shared", "Advance pending", "Booked", "Lost"],
        "first_status": "New event inquiry",
        "first_action": "Confirm event date, location, and package interest",
        "messages": {
            "first_reply": "Hi {name}, thanks for reaching out. Please share your event date and location so I can confirm availability for {service}.",
            "follow_up": "Hi {name}, following up on the {service} package. I can block the date once the advance is confirmed.",
            "payment": "Hi {name}, gentle reminder that Rs. {amount} is pending for {service}. Please share confirmation after payment.",
        },
    },
    "agency": {
        "label": "Freelancer / Agency",
        "statuses": ["New inquiry", "Discovery booked", "Proposal sent", "Follow-up due", "Won", "Lost"],
        "first_status": "New inquiry",
        "first_action": "Send discovery call options and capture project scope",
        "messages": {
            "first_reply": "Hi {name}, thanks for your inquiry. I can help with {service}. Would you like to schedule a short discovery call?",
            "follow_up": "Hi {name}, checking in on the proposal for {service}. Happy to clarify scope, timeline, or pricing.",
            "payment": "Hi {name}, gentle reminder that Rs. {amount} is pending for the {service} milestone.",
        },
    },
}


def fill_template(template, **kwargs):
    output = template
    for key, value in kwargs.items():
        output = output.replace("{" + key + "}", str(value or ""))
    return output
