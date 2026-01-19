# 🔐 ADDING YOUR API KEY TO STREAMLIT CLOUD

## IMPORTANT: Your app needs your API key to work!

**This is NORMAL and SECURE** - we removed the API key from the code (GitHub caught it, which is good!).

Now you'll add it securely through Streamlit's encrypted secrets system.

---

## Step-by-Step (2 minutes)

### Step 1: Deploy Your App First

1. Upload the clean ZIP to GitHub (no more secret scanning errors!)
2. Deploy to Streamlit Cloud as normal
3. Your app will load but show an error - **this is expected**

### Step 2: Add Your API Key Securely

1. In Streamlit Cloud, go to your app
2. Click **"⚙️ Settings"** (top right corner)
3. Click **"Secrets"** from the menu
4. Paste this into the secrets editor:

```toml
ANTHROPIC_API_KEY = "your-api-key-here"
```

**Replace `your-api-key-here` with your actual Anthropic API key**

(You have this key - it starts with `sk-ant-api03-...`)

5. Click **"Save"**

### Step 3: App Restarts Automatically

- Streamlit detects the new secret
- App restarts (takes 10 seconds)
- **Now it works!** ✅

---

## Why This Method?

**✅ SECURE**: API key is encrypted in Streamlit's vault  
**✅ SAFE**: Key is NOT in your code or GitHub  
**✅ PRIVATE**: Only you can see it  
**✅ EASY**: Change it anytime in Settings  

**❌ NEVER**: Put API keys directly in code  
**❌ NEVER**: Commit API keys to GitHub  

---

## Troubleshooting

**"Secret not found" error?**
- Make sure you clicked "Save" after pasting
- Check the format matches exactly (with quotes)
- Wait 10 seconds for restart

**Still not working?**
- Check the secret name is exactly: `ANTHROPIC_API_KEY`
- Check your API key is valid at: https://console.anthropic.com

---

**Your factory will work perfectly once this is set up!** 🚀
