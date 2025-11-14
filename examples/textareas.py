"""Textarea showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Textarea


def build_textareas_showcase():
    """Build comprehensive textarea showcase content."""
    return html.div(
        # Section 1: Basic Textareas
        html.h2(
            "Basic Textareas",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Multi-line text input fields for comments, descriptions, and messages.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                Textarea(
                    id="comment",
                    label="Your comment",
                    placeholder="Write your thoughts here...",
                ),
                class_="mb-4",
            ),
            html.div(
                Textarea(
                    id="message",
                    label="Message",
                    placeholder="Leave a message...",
                    rows=6,
                ),
                class_="mb-4",
            ),
            html.div(
                Textarea(
                    id="bio",
                    label="Biography",
                    value="Software engineer passionate about Python and web development.",
                    helper_text="This will be displayed on your public profile",
                ),
                class_="mb-4",
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 2: Validation States
        html.h2(
            "Validation States",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Textareas with success and error validation states.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                Textarea(
                    id="review_success",
                    label="Product Review",
                    validation="success",
                    helper_text="Thank you for your detailed review!",
                    value="This product exceeded my expectations. Highly recommended!",
                    rows=3,
                ),
                class_="mb-4",
            ),
            html.div(
                Textarea(
                    id="feedback_error",
                    label="Feedback",
                    validation="error",
                    helper_text="Feedback must be at least 20 characters long",
                    value="Too short",
                    rows=3,
                ),
                class_="mb-4",
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 3: Required Fields
        html.h2(
            "Required Fields",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Required textareas show asterisk in label for visual indication.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                Textarea(
                    id="description_required",
                    label="Product Description",
                    placeholder="Describe your product in detail...",
                    required=True,
                    helper_text="This field is required",
                    rows=5,
                ),
                class_="mb-4",
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 4: Disabled State
        html.h2(
            "Disabled State",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Disabled textareas cannot be edited (grayed out).",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            Textarea(
                id="locked_content",
                label="Original Submission",
                value="This content cannot be modified because it has been locked.",
                disabled=True,
                rows=3,
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 5: Readonly State
        html.h2(
            "Readonly State",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Readonly textareas can be focused and copied but not edited.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            Textarea(
                id="terms",
                label="Terms and Conditions",
                value="By using this service, you agree to our terms and conditions...",
                readonly=True,
                rows=4,
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 6: Different Sizes
        html.h2(
            "Different Sizes",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Control textarea height with rows parameter.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.div(
                Textarea(
                    id="quick_note",
                    label="Quick Note (3 rows)",
                    placeholder="Short note...",
                    rows=3,
                ),
                class_="mb-4",
            ),
            html.div(
                Textarea(
                    id="medium_text",
                    label="Medium Text (6 rows)",
                    placeholder="Medium length content...",
                    rows=6,
                ),
                class_="mb-4",
            ),
            html.div(
                Textarea(
                    id="long_essay",
                    label="Long Essay (12 rows)",
                    placeholder="Write a detailed essay...",
                    rows=12,
                ),
                class_="mb-4",
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        # Section 7: Form Example
        html.h2(
            "Complete Form Example",
            class_="text-2xl font-bold mb-4 text-gray-900 dark:text-white",
        ),
        html.p(
            "Contact form with multiple textareas demonstrating real-world usage.",
            class_="mb-4 text-gray-600 dark:text-gray-400",
        ),
        html.div(
            html.form(
                Textarea(
                    id="contact_name",
                    label="Your Name",
                    name="name",
                    placeholder="John Doe",
                    required=True,
                    rows=1,
                ),
                html.div(class_="mb-4"),
                Textarea(
                    id="contact_subject",
                    label="Subject",
                    name="subject",
                    placeholder="How can we help?",
                    required=True,
                    rows=2,
                ),
                html.div(class_="mb-4"),
                Textarea(
                    id="contact_message",
                    label="Message",
                    name="message",
                    placeholder="Tell us more...",
                    required=True,
                    helper_text="Please provide as much detail as possible",
                    rows=8,
                ),
                html.div(class_="mb-4"),
                html.button(
                    "Send Message",
                    type="submit",
                    class_="px-5 py-2.5 text-sm font-medium text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 rounded-lg dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
                ),
                method="post",
                action="/contact/submit",
            ),
            class_="bg-white dark:bg-gray-800 rounded-lg p-6 mb-8 shadow",
        ),
        class_="container mx-auto px-4 py-8",
    )


# Standalone app entry point
if __name__ == "__main__":
    import uvicorn
    from fastapi import FastAPI
    from fasthx.jinja import Jinja
    from fastapi.templating import Jinja2Templates

    app = FastAPI()
    templates = Jinja2Templates(directory="examples/templates")
    jinja = Jinja(templates)

    @app.get("/")
    async def root():
        """Render textareas showcase."""
        return jinja.template(
            "showcase.html.jinja",
            title="Textareas - Flowbite HTMY Showcase",
            content=build_textareas_showcase(),
        )

    print("🚀 Textarea Showcase running at http://localhost:8000")
    print("📖 View all textarea examples in your browser")
    uvicorn.run(app, host="127.0.0.1", port=8000)
