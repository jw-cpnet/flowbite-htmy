"""Inputs showcase content for consolidated app."""

from htmy import html

from flowbite_htmy.components import Input


def build_inputs_showcase():
    """Build comprehensive inputs showcase content.

    Extracted for reuse in consolidated showcase application.
    Returns htmy Component ready for rendering.
    """
    return html.div(
        # Basic input fields
        html.h2(
            "Basic input fields",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-8",
        ),
        html.p(
            "Use these examples of input fields for different types of data including text, email, password, number, URL, and phone number.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Input(
                    id="first_name",
                    label="First name",
                    placeholder="John",
                    required=True,
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="last_name",
                    label="Last name",
                    placeholder="Doe",
                    required=True,
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="email",
                    label="Email address",
                    type="email",
                    placeholder="john.doe@company.com",
                    required=True,
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="password",
                    label="Password",
                    type="password",
                    placeholder="•••••••••",
                    required=True,
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="phone",
                    label="Phone number",
                    type="tel",
                    placeholder="123-45-678",
                    attrs={"pattern": "[0-9]{3}-[0-9]{2}-[0-9]{3}"},
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="website",
                    label="Website URL",
                    type="url",
                    placeholder="flowbite.com",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="visitors",
                    label="Number of visitors",
                    type="number",
                    placeholder="1000",
                ),
            ),
        ),
        # Input with helper text
        html.h2(
            "Input with helper text",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use helper text to provide additional context or instructions for the input field.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            Input(
                id="email_help",
                label="Your email",
                type="email",
                placeholder="name@flowbite.com",
                helper_text="We'll never share your details. Read our Privacy Policy.",
            ),
        ),
        # Required fields
        html.h2(
            "Required fields",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use the required attribute to indicate mandatory fields to users.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Input(
                    id="required_email",
                    label="Email",
                    type="email",
                    placeholder="name@flowbite.com",
                    required=True,
                    helper_text="This field is required",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="required_password",
                    label="Password",
                    type="password",
                    placeholder="•••••••••",
                    required=True,
                    helper_text="Must be at least 8 characters",
                ),
            ),
        ),
        # Disabled state
        html.h2(
            "Disabled state",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use the disabled attribute to indicate that an input field cannot be edited.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Input(
                    id="disabled_input",
                    label="Disabled input",
                    value="Disabled input",
                    disabled=True,
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="disabled_readonly",
                    label="Disabled readonly input",
                    value="Disabled readonly input",
                    disabled=True,
                    attrs={"readonly": True},
                ),
            ),
        ),
        # Validation - Success
        html.h2(
            "Validation",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use validation states to provide feedback on form submission or field validation.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Input(
                    id="success_input",
                    label="Your name",
                    validation="success",
                    placeholder="Success input",
                    helper_text="Well done! Username is available.",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="error_input",
                    label="Your name",
                    validation="error",
                    placeholder="Error input",
                    helper_text="Oh, snap! Username is already taken.",
                ),
            ),
        ),
        # Input types
        html.h2(
            "Input types",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Use different input types for various data formats including text, email, password, number, tel, and url.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.div(
            html.div(
                Input(
                    id="input_text",
                    label="Text",
                    type="text",
                    placeholder="Text input",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="input_email",
                    label="Email",
                    type="email",
                    placeholder="name@example.com",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="input_password",
                    label="Password",
                    type="password",
                    placeholder="•••••••••",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="input_number",
                    label="Number",
                    type="number",
                    placeholder="123",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="input_tel",
                    label="Phone",
                    type="tel",
                    placeholder="123-456-7890",
                ),
                class_="mb-6",
            ),
            html.div(
                Input(
                    id="input_url",
                    label="Website",
                    type="url",
                    placeholder="https://example.com",
                ),
            ),
        ),
        # Complex form example
        html.h2(
            "Registration form example",
            class_="text-2xl font-bold text-gray-900 dark:text-white mb-4 mt-12",
        ),
        html.p(
            "Complete registration form demonstrating various input types and validation.",
            class_="text-gray-600 dark:text-gray-400 mb-6",
        ),
        html.form(
            html.div(
                html.div(
                    Input(
                        id="reg_first_name",
                        label="First name",
                        placeholder="John",
                        required=True,
                    ),
                ),
                html.div(
                    Input(
                        id="reg_last_name",
                        label="Last name",
                        placeholder="Doe",
                        required=True,
                    ),
                ),
                html.div(
                    Input(
                        id="reg_email",
                        label="Email",
                        type="email",
                        placeholder="john.doe@company.com",
                        required=True,
                        helper_text="We'll use this for account verification",
                    ),
                ),
                html.div(
                    Input(
                        id="reg_password",
                        label="Password",
                        type="password",
                        placeholder="•••••••••",
                        required=True,
                        helper_text="Must be at least 8 characters with uppercase, lowercase and numbers",
                    ),
                ),
                html.div(
                    Input(
                        id="reg_confirm_password",
                        label="Confirm password",
                        type="password",
                        placeholder="•••••••••",
                        required=True,
                    ),
                ),
                html.div(
                    Input(
                        id="reg_phone",
                        label="Phone number (optional)",
                        type="tel",
                        placeholder="123-456-7890",
                    ),
                ),
                class_="grid gap-6 mb-6 md:grid-cols-2",
            ),
            html.button(
                "Submit",
                type="submit",
                class_="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:outline-none focus:ring-blue-300 font-medium rounded-lg text-sm w-full sm:w-auto px-5 py-2.5 text-center dark:bg-blue-600 dark:hover:bg-blue-700 dark:focus:ring-blue-800",
            ),
        ),
        class_="space-y-8",
    )
