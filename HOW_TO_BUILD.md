# How to Turn This Into an Installable Android App (No Coding Required)

You will use GitHub's free build robot to compile the app into a real APK
file. This takes about 10-15 minutes of clicking, and about 10-15 minutes
of waiting for the build to finish.

## Step 1: Create a free GitHub account
Go to https://github.com/signup if you don't already have an account.

## Step 2: Create a new repository
1. Click the "+" icon (top right) -> "New repository"
2. Name it anything, e.g. `florence-quote-app`
3. Set it to **Public** (required for free builds)
4. Click "Create repository"

## Step 3: Upload these files
On your new repository page:
1. Click "Add file" -> "Upload files"
2. Drag in ALL of these files/folders, keeping the folder structure:
   - `main.py`
   - `buildozer.spec`
   - `.github/workflows/build.yml`
3. Click "Commit changes"

(Tip: GitHub's upload page lets you drag a whole folder at once - it will
preserve the `.github/workflows/build.yml` path automatically.)

## Step 4: Let it build
1. Go to the "Actions" tab at the top of your repository
2. You'll see "Build Android APK" running (a yellow dot = in progress)
3. Wait for it to turn into a green checkmark (~10-15 minutes)

## Step 5: Download your APK
1. Click on the finished build (green checkmark)
2. Scroll down to "Artifacts"
3. Click "florence-quote-calculator-apk" to download a zip
4. Unzip it - inside is your `.apk` file

## Step 6: Install it on your phone
1. Transfer the `.apk` file to your Android phone (email it to yourself,
   or use a USB cable/Google Drive)
2. Open it on your phone - Android may ask you to allow "install from
   unknown sources" the first time. Allow it.
3. Tap install. Done - the app icon will appear like any other app.

---

**Whenever you want a change** (new field, different design, extra fee
type), just tell Claude what you want. Claude will update `main.py`,
you re-upload the changed file to the same GitHub repo (Step 3), and it
automatically rebuilds a new APK.
