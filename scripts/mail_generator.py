def create_inbox_hook(top_article_title, summary_snippet):
    # Professional, high-signal subject line
    subject = f"Agentic Pulse | {top_article_title}"
    
    # Hidden preheader to control the text following the subject line in the inbox
    # The &zwnj; hack prevents the email client from pulling random text from the body
    preheader = f"""
    <div style="display: none; max-height: 0px; overflow: hidden;">
        Weekly Intel: {summary_snippet[:120]}...
        &nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;&zwnj;&nbsp;
    </div>
    """
    return subject, preheader

def generate_newsletter_html(articles, week_label):
    # Base Styles (Inline for Email Compatibility)
    body_bg = "#f8fafc"
    card_bg = "#ffffff"
    text_main = "#0f172a"
    text_muted = "#64748b"
    accent_blue = "#2563eb"
    
    # Start building the HTML
    html = f"""
    <div style="background-color: {body_bg}; padding: 40px 10px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
        <table align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; background-color: {card_bg}; border-radius: 24px; border: 1px solid #e2e8f0; overflow: hidden;">
            <tr>
                <td style="padding: 40px; border-bottom: 1px solid #f1f5f9;">
                    <span style="background: {accent_blue}; color: #ffffff; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 800; text-transform: uppercase; letter-spacing: 0.05em;">Weekly Intelligence</span>
                    <h1 style="font-size: 24px; font-weight: 800; color: {text_main}; margin: 16px 0 8px 0; letter-spacing: -0.02em;">{week_label}</h1>
                    <p style="color: {text_muted}; font-size: 15px; margin: 0;">A curated synthesis of Agentic AI breakthroughs for architects and CTOs.</p>
                </td>
            </tr>
            <tr>
                <td style="padding: 40px;">
    """

    # Loop through articles and create "Slick" cards
    for art in articles:
        html += f"""
                    <div style="margin-bottom: 40px; border-bottom: 1px solid #f8fafc; padding-bottom: 30px;">
                        <span style="color: {accent_blue}; font-size: 11px; font-weight: 700; text-transform: uppercase;">[{art['tag']}]</span>
                        <h2 style="font-size: 19px; font-weight: 800; color: {text_main}; margin: 8px 0 12px 0; line-height: 1.3;">{art['title']}</h2>
                        <p style="color: #475569; font-size: 15px; line-height: 1.6; margin-bottom: 16px;">
                            {art['summary']}
                        </p>
                        <a href="{art['url']}" style="color: {accent_blue}; font-weight: 700; text-decoration: none; font-size: 14px;">Read Full Briefing →</a>
                    </div>
        """

    # Footer
    html += f"""
                </td>
            </tr>
            <tr>
                <td style="padding: 30px 40px; background: #fbfcfd; text-align: center; border-top: 1px solid #f1f5f9;">
                    <p style="color: {text_muted}; font-size: 12px; margin-bottom: 8px;">&copy; 2025 Agentic Pulse. All rights reserved.</p>
                    <a href="#" style="color: {text_muted}; font-size: 12px; text-decoration: underline;">Unsubscribe</a>
                </td>
            </tr>
        </table>
    </div>
    """
    return html