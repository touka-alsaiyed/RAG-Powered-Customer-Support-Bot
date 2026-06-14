# Real customer service documents for RAG system
# These mimic actual company documentation

DOCUMENTS = [
    {
        "id": "return_policy_1",
        "title": "Return & Refund Policy",
        "content": """
        Returns are accepted within 30 days of purchase for most items.
        Items must be in original condition with all packaging and tags attached.
        Electronics must not show signs of use. To start a return:
        1. Go to your order history
        2. Click "Return Item"
        3. Select reason for return
        4. Print shipping label (prepaid)
        5. Ship back to us
        Refunds are processed within 5-7 business days after we receive the item.
        Non-returnable items: underwear, swimwear, pierced jewelry, custom orders.
        Shipping costs are non-refundable unless the return is due to our error.
        """
    },
    {
        "id": "shipping_1",
        "title": "Shipping & Delivery",
        "content": """
        Shipping Options:
        - Standard Shipping: 5-7 business days (FREE on orders over $50)
        - Express Shipping: 2-3 business days ($9.99)
        - Overnight Shipping: Next business day ($24.99)
        - Same-day delivery available in selected cities ($15.99)
        
        Processing time: Orders are processed within 24 hours of purchase.
        International shipping: Available to 150+ countries, 10-21 business days.
        
        Free shipping doesn't apply to:
        - Heavy items (over 50 lbs)
        - Furniture delivery
        - White glove delivery
        
        Track your order: Check your confirmation email for tracking number.
        Orders placed after 2 PM EST ship the next business day.
        """
    },
    {
        "id": "password_reset_1",
        "title": "Account & Password Help",
        "content": """
        Forgot your password?
        1. Go to the login page
        2. Click "Forgot Password?"
        3. Enter your email address
        4. Check your email (including spam folder)
        5. Click the reset link (valid for 24 hours)
        6. Create a new password (minimum 8 characters, must include 1 number and 1 symbol)
        
        Two-Factor Authentication:
        For added security, enable 2FA in Account Settings.
        After login, you'll receive a code via SMS or email to verify.
        
        Account locked?
        If you enter the wrong password 5 times, your account locks for 30 minutes.
        Contact support if you can't unlock your account.
        
        Update email address:
        Go to Settings > Email > Verify New Email > Confirm from link sent to new email.
        """
    },
    {
        "id": "payment_methods_1",
        "title": "Payment Methods & Billing",
        "content": """
        Accepted Payment Methods:
        - Credit/Debit cards: Visa, Mastercard, American Express, Discover
        - Digital wallets: Apple Pay, Google Pay, PayPal
        - Buy Now, Pay Later: Klarna, Affirm (4 interest-free payments)
        - Bank transfers (ACH) for orders over $500
        
        Billing Address:
        Must match your shipping address for fraud prevention.
        If different, provide proof of residence.
        
        Declined Payment?
        Check:
        - Sufficient funds
        - Card hasn't expired
        - Card issuer hasn't flagged the transaction
        - ZIP code matches your bank records
        
        Invoice:
        Digital invoice sent to email within 2 hours of purchase.
        Request printed invoice in Account > Order History.
        
        Billing Questions:
        Contact billing@support.com or call 1-800-555-0123
        """
    },
    {
        "id": "product_warranty_1",
        "title": "Warranty & Product Coverage",
        "content": """
        Manufacturer Warranty:
        All electronics come with a 1-year manufacturer's warranty covering defects.
        Warranty covers: manufacturing defects, failure due to normal use
        Warranty does NOT cover: accidental damage, water damage, physical damage, normal wear
        
        Accidental Damage Protection (ADP):
        Optional $29.99 protection plan covers:
        - Accidental drops and impacts
        - Liquid damage
        - Mechanical failures
        - Can be purchased up to 30 days after purchase
        - Covers up to 2 incidents
        
        How to claim warranty:
        1. Contact support with proof of purchase
        2. Describe the issue
        3. Perform troubleshooting steps if requested
        4. Ship item to us (prepaid label provided)
        5. Repair or replacement within 10 business days
        
        Furniture warranty:
        1-year warranty against manufacturing defects.
        Covers structural frame, springs, and hardware.
        Does not cover stains, pet damage, or wear.
        """
    },
    {
        "id": "subscription_1",
        "title": "Subscription Management",
        "content": """
        Subscribe & Save Program:
        Save 15% when you subscribe to regular deliveries.
        
        How it works:
        1. Select delivery frequency (every 2/4/6/8 weeks)
        2. Get automatic shipments on your schedule
        3. No commitment - cancel anytime
        4. Skip a delivery from your dashboard
        5. Change frequency or quantity anytime
        
        Subscription pricing:
        - First order: 15% discount
        - Subsequent orders: 15% discount
        - Cancel anytime before next billing date
        
        Pause subscription:
        Log in > Subscriptions > Pause (up to 3 months)
        
        Billing:
        Charged 3 days before each shipment.
        You'll receive email reminder 7 days before billing.
        Cancel email reminders anytime in settings.
        """
    },
    {
        "id": "contact_preferences_1",
        "title": "Contact Preferences & Communication",
        "content": """
        Manage Your Communication:
        Go to Account > Communication Preferences to control what you receive:
        
        Email:
        - Order updates: Sent automatically, cannot be turned off
        - Promotional emails: Opt in/out anytime
        - Product recommendations: Based on browsing history
        - Newsletter: Weekly deals and new products
        
        SMS Notifications:
        - Opt in during checkout
        - Receive order updates, delays, and delivery confirmations
        - Standard text message rates apply
        - Unsubscribe by replying STOP to any message
        
        Push Notifications (Mobile App):
        - Order tracking
        - Flash sales
        - Personalized recommendations
        - Turn off in app settings
        
        Do Not Call Registry:
        We respect the National Do Not Call Registry.
        If called, let us know and we'll add you to our internal list.
        """
    },
    {
        "id": "delivery_issues_1",
        "title": "Delivery Issues & Lost Packages",
        "content": """
        Package not arrived?
        Standard Shipping: Check status 7 days after order.
        Express/Overnight: Contact us after 24 hours of delivery date.
        
        What to do:
        1. Check your tracking number for updates
        2. Confirm correct delivery address on original order
        3. Ask neighbors/building manager if it was left nearby
        4. Contact carrier (UPS/FedEx/USPS) for delivery confirmation
        5. File a claim with us if package was marked delivered but not found
        
        Package marked delivered but not received:
        - File claim within 48 hours
        - Include photos if available
        - Provide tracking number
        - We investigate with carrier within 5-7 business days
        
        Damaged package:
        - Report within 48 hours of delivery
        - Take photos of damage
        - Keep original packaging
        - We'll send replacement or refund
        
        Weather delays:
        Severe weather may delay shipments by 1-3 days.
        Check tracking for updates.
        
        Refund for lost package:
        Full refund processed if carrier confirms loss.
        Takes 7-10 business days after carrier determination.
        """
    },
    {
        "id": "bulk_orders_1",
        "title": "Bulk & Business Orders",
        "content": """
        Bulk Ordering Program:
        For orders 25+ units, we offer:
        - Custom pricing (typically 20-30% off)
        - Dedicated account manager
        - Flexible payment terms (Net 30 available)
        - Priority fulfillment
        - Free shipping on orders over $2,000
        
        How to request bulk quote:
        1. Call 1-800-555-0456 (Business Sales)
        2. Email bulk@company.com with:
           - Product SKU or name
           - Quantity needed
           - Desired delivery date
           - Your business name and tax ID
        3. Provide your own packaging requirements
        
        Bulk pricing tiers:
        - 25-99 units: 20% discount
        - 100-499 units: 25% discount
        - 500+ units: Custom quote
        
        Minimum order value: $500
        Lead time: 5-10 business days for standard items
        Custom items: 15-30 business days
        
        Invoicing:
        Monthly consolidated invoices available.
        Net 30 terms for approved business accounts.
        """
    },
    {
        "id": "quality_guarantee_1",
        "title": "Quality Guarantee & Satisfaction Promise",
        "content": """
        100% Satisfaction Guarantee:
        If you're not completely satisfied, we make it right.
        
        Our Promise:
        - If product is defective, we replace it free
        - If product doesn't match description, full refund
        - If you change your mind, 30-day returns
        - If damaged in shipping, we cover it
        
        No questions asked return option:
        Return any item within 30 days for full refund.
        Even if you've used it, changed your mind, or no longer want it.
        (Exception: custom/made-to-order items are final sale)
        
        Extended warranty:
        2-year coverage available for $39.99 on electronics.
        Covers accidental damage, hardware failure, and water damage.
        
        Lifetime guarantees on:
        - Premium cookware (covers manufacturing defects)
        - Leather goods (covers defects in materials/craftsmanship)
        - Bedding (covers defective seams/zippers for 10 years)
        
        Quality standards:
        All products inspected before shipping.
        If you receive damaged item, we replace at no cost.
        """
    }
]