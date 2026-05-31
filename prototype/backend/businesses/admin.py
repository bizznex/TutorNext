from django.contrib import admin

from .models import (
    Business,
    Catalogue,
    CatalogueItem,
    Customer,
    CaseStudy,
    FAQ,
    FollowUpTask,
    Inquiry,
    Lead,
    MediaAsset,
    MessageTemplate,
    OperatorNote,
    PageEvent,
    Payment,
    ScoreReason,
    ScoreSnapshot,
    SetupProject,
    Testimonial,
    TrustProof,
)

admin.site.register(Business)
admin.site.register(SetupProject)
admin.site.register(Catalogue)
admin.site.register(CatalogueItem)
admin.site.register(FAQ)
admin.site.register(TrustProof)
admin.site.register(MediaAsset)
admin.site.register(Testimonial)
admin.site.register(CaseStudy)
admin.site.register(PageEvent)
admin.site.register(Inquiry)
admin.site.register(Lead)
admin.site.register(FollowUpTask)
admin.site.register(Customer)
admin.site.register(Payment)
admin.site.register(MessageTemplate)
admin.site.register(ScoreSnapshot)
admin.site.register(ScoreReason)
admin.site.register(OperatorNote)
