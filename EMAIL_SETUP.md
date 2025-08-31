# 📧 Email Functionality Setup Guide

## Overview
The Match Simulator app now includes email functionality that allows admins to send emails to all users or specific user groups. This feature uses the email addresses provided by users during signup.

## 🚀 Features

### ✅ What's Available
- **Send emails to all users** - Broadcast announcements to everyone
- **Targeted emails** - Send to specific user groups:
  - Only approved users
  - Only pending users
  - Only admin users
  - Only regular users
- **Email templates** - Pre-built templates for common scenarios
- **Test functionality** - Test your email configuration before sending
- **Email history** - Track all sent emails with audit trail
- **Security features** - Confirmation dialogs and recipient counts

### 📧 Email Templates
1. **Welcome Message** - For new users
2. **Maintenance Notice** - System maintenance announcements
3. **Update Announcement** - New features and improvements
4. **Event Reminder** - Upcoming events and reminders
5. **Custom Message** - Your own custom content

## 🔧 Setup Instructions

### Gmail Setup (Recommended)

1. **Enable 2-Factor Authentication**
   - Go to your Google Account settings
   - Navigate to Security → 2-Step Verification
   - Enable 2-Factor Authentication

2. **Generate App Password**
   - In Security settings, go to 2-Step Verification → App passwords
   - Select "Mail" as the app
   - Click "Generate"
   - Copy the 16-character password

3. **Use in App**
   - Email: Your Gmail address
   - Password: The generated app password (not your regular Gmail password)

### Other Email Providers

#### Outlook/Hotmail
- SMTP Server: `smtp-mail.outlook.com`
- Port: `587`
- Use your email password or app password

#### Yahoo
- SMTP Server: `smtp.mail.yahoo.com`
- Port: `587`
- Use your email password or app password

#### Custom SMTP
- Contact your email provider for SMTP settings
- Common ports: 587 (TLS), 465 (SSL), 25 (unencrypted)

## 📱 How to Use

### Accessing Email Functionality
1. Login as an admin user
2. Navigate to "📧 Send Email to Users" in the sidebar
3. Configure your email settings
4. Choose recipients and compose your message
5. Test your configuration first
6. Send to all users

### Step-by-Step Process

1. **Email Configuration**
   - Enter your admin email address
   - Enter your email password/app password
   - Verify SMTP server and port (defaults work for most providers)

2. **Recipient Selection**
   - Choose who should receive the email
   - See real-time recipient count

3. **Message Composition**
   - Select a template or write custom content
   - Preview your message
   - Verify recipient count

4. **Testing**
   - Use "Test Email Configuration" to verify setup
   - Check your inbox for the test email

5. **Sending**
   - Confirm recipient count
   - Check the confirmation box
   - Send to all selected users

## ⚠️ Important Notes

### Security
- **Never use regular Gmail passwords** - Use app passwords
- Test your configuration before sending to all users
- Emails are sent from your admin account
- All email actions are logged for audit purposes

### Best Practices
- Test with a small group first
- Use clear, professional subject lines
- Keep messages concise and relevant
- Monitor email delivery success rates

### Limitations
- Users without email addresses won't receive emails
- Email delivery depends on recipient email providers
- Some emails may be marked as spam
- Large recipient lists may take time to process

## 🐛 Troubleshooting

### Common Issues

#### Authentication Failed
- Verify your email and password
- For Gmail: Use app password, not regular password
- Check if 2FA is enabled

#### Connection Failed
- Verify SMTP server and port
- Check firewall settings
- Try different ports (587, 465, 25)

#### Emails Not Delivered
- Check spam/junk folders
- Verify recipient email addresses
- Check email provider restrictions

### Getting Help
1. Test your configuration first
2. Check the error messages in the app
3. Verify your email provider settings
4. Ensure recipient emails are valid

## 📊 Monitoring

### Email Statistics
- Total users in system
- Users with email addresses
- Users without email addresses

### Email History
- Track all sent emails
- View recipient counts
- Monitor sending patterns
- Audit trail for compliance

## 🔒 Privacy & Compliance

### Data Protection
- Only admins can send emails
- User emails are stored securely
- Email content is logged for audit purposes
- Recipients can unsubscribe by contacting admin

### Compliance
- Follow email marketing best practices
- Respect user privacy preferences
- Maintain audit trails for business purposes
- Comply with local email regulations

---

**Need Help?** Contact your system administrator or refer to the email provider's documentation for specific setup instructions.
