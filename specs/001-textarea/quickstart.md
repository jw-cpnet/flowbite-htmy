# Textarea Component - Quickstart Guide

**Date**: 2025-11-14
**Component**: `flowbite_htmy.components.Textarea`

## Installation

```bash
pip install flowbite-htmy
```

## Basic Usage

### Minimal Example

The simplest textarea with just an ID and label:

```python
from flowbite_htmy.components import Textarea

textarea = Textarea(
    id="comment",
    label="Your comment",
)
```

**Renders**:
```html
<div class="">
  <label for="comment" class="block mb-2 text-sm font-medium text-gray-900 dark:text-white">
    Your comment
  </label>
  <textarea
    id="comment"
    rows="4"
    class="block p-2.5 w-full text-sm rounded-lg border bg-gray-50 text-gray-900 border-gray-300 focus:ring-blue-500 focus:border-blue-500 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500">
  </textarea>
</div>
```

### With Placeholder

Add placeholder text for guidance:

```python
textarea = Textarea(
    id="feedback",
    label="Feedback",
    placeholder="Write your thoughts here...",
)
```

### With Helper Text

Provide additional context below the textarea:

```python
textarea = Textarea(
    id="bio",
    label="Biography",
    placeholder="Tell us about yourself",
    helper_text="Maximum 500 characters. This will be displayed on your public profile.",
)
```

## Validation States

### Success State

Show positive feedback with green styling:

```python
textarea = Textarea(
    id="review",
    label="Product Review",
    validation="success",
    helper_text="Thank you for your detailed review!",
    value="This product exceeded my expectations...",
)
```

### Error State

Show validation errors with red styling:

```python
textarea = Textarea(
    id="message",
    label="Message",
    validation="error",
    helper_text="Message must be at least 10 characters long.",
    value="Too short",
)
```

## Edit Forms (Pre-filled Values)

For editing existing content, use the `value` prop:

```python
# Editing user bio
existing_bio = "Software engineer passionate about Python and web development."

textarea = Textarea(
    id="user_bio",
    label="Edit Biography",
    value=existing_bio,
    rows=6,
)
```

## Required Fields

Mark fields as required with automatic asterisk indicator:

```python
textarea = Textarea(
    id="description",
    label="Product Description",  # Will display as "Product Description *"
    required=True,
    placeholder="Describe your product in detail",
)
```

**Renders label as**: "Product Description *"

## Sizing Control

### Custom Row Count

Adjust the visible height:

```python
# Short comment box (3 rows)
textarea = Textarea(
    id="quick_note",
    label="Quick Note",
    rows=3,
)

# Long essay box (10 rows)
textarea = Textarea(
    id="essay",
    label="Essay",
    rows=10,
)
```

### Custom Width

Use `class_` to control width:

```python
# Half width
textarea = Textarea(
    id="sidebar_note",
    label="Notes",
    class_="w-1/2",
)

# Specific pixel width
textarea = Textarea(
    id="fixed_width",
    label="Comment",
    class_="max-w-md",
)
```

## Disabled State

Prevent interaction with grayed-out styling:

```python
textarea = Textarea(
    id="locked_content",
    label="Original Submission",
    value="This content cannot be modified.",
    disabled=True,
)
```

## Readonly State

Allow viewing and copying but prevent editing:

```python
textarea = Textarea(
    id="terms",
    label="Terms and Conditions",
    value="By using this service, you agree to...",
    readonly=True,
    rows=10,
)
```

## Form Submission

### With Name Attribute

For traditional form submission:

```python
textarea = Textarea(
    id="feedback_text",
    label="Feedback",
    name="feedback",  # Form submission key
    required=True,
)
```

**Submitted as**: `feedback=<user input>`

### HTMX Integration

For dynamic updates without page reload:

```python
textarea = Textarea(
    id="live_comment",
    label="Comment",
    placeholder="Type your comment...",
    hx_post="/api/comments",
    hx_trigger="blur",  # Submit on blur
    hx_target="#comment-list",
    hx_swap="afterbegin",
)
```

**Behavior**: Posts to `/api/comments` when user clicks outside textarea, prepending result to `#comment-list`.

## Complete Example

Combining multiple features:

```python
from flowbite_htmy.components import Textarea

# Contact form message field
message_field = Textarea(
    id="contact_message",
    label="Message",
    name="message",
    placeholder="How can we help you?",
    rows=6,
    required=True,
    helper_text="Please provide as much detail as possible.",
    hx_post="/api/contact/validate",
    hx_trigger="blur",
    hx_target="#message-validation",
)

# Blog post editor with pre-filled content
blog_editor = Textarea(
    id="post_content",
    label="Blog Post Content",
    name="content",
    value=existing_post_content,  # Variable from database
    rows=15,
    required=True,
    class_="font-mono",  # Monospace font for markdown editing
)

# Read-only system message
system_message = Textarea(
    id="system_msg",
    label="System Log",
    value=log_content,
    rows=8,
    readonly=True,
    class_="max-w-2xl",
)
```

## With FastAPI + Jinja

Integration in FastAPI application:

```python
# app.py
from fastapi import FastAPI
from fasthx import Jinja
from flowbite_htmy.components import Textarea

app = FastAPI()
jinja = Jinja(app)

@app.get("/contact")
async def contact_page():
    message_field = Textarea(
        id="message",
        label="Your Message",
        name="message",
        placeholder="What would you like to say?",
        rows=5,
        required=True,
        helper_text="We typically respond within 24 hours.",
    )

    return jinja.template(
        "contact.html.jinja",
        message_field=message_field,
    )
```

```jinja
<!-- templates/contact.html.jinja -->
<!DOCTYPE html>
<html>
<body>
  <form method="post" action="/contact/submit">
    <!-- Render the textarea component -->
    {{ message_field }}

    <button type="submit" class="mt-4 px-4 py-2 bg-blue-600 text-white rounded-lg">
      Send Message
    </button>
  </form>
</body>
</html>
```

## Advanced: Custom Attributes

Pass additional HTML attributes via `attrs`:

```python
textarea = Textarea(
    id="code_input",
    label="Code",
    attrs={
        "spellcheck": "false",
        "autocomplete": "off",
        "maxlength": "1000",
    },
)
```

**Renders**: `<textarea id="code_input" spellcheck="false" autocomplete="off" maxlength="1000" ...></textarea>`

## Testing

Example test for textarea component:

```python
import pytest
from htmy import Renderer
from flowbite_htmy.components import Textarea

@pytest.mark.asyncio
async def test_textarea_default():
    renderer = Renderer()

    textarea = Textarea(
        id="test",
        label="Test Field",
    )

    html = await renderer.render(textarea)

    assert 'id="test"' in html
    assert 'Test Field' in html
    assert 'rows="4"' in html  # Default rows
    assert 'block p-2.5 w-full' in html  # Base classes
```

---

**Quickstart Version**: 1.0.0
**Last Updated**: 2025-11-14
**Next**: See [textarea-api.md](./contracts/textarea-api.md) for complete API reference
