/**
 * flowbite-htmy.js - Initialization code for Flowbite components
 *
 * This file handles initialization of Flowbite components used by flowbite-htmy.
 * It should be included in your HTML after Flowbite's main JS file.
 */

(function() {
    'use strict';

    // Toast management configuration
    const TOAST_CONFIG = {
        maxToasts: 5,           // Maximum toasts in container
        autoDismissDelay: 5000  // Auto-dismiss after 5 seconds (0 = disabled)
    };

    /**
     * Initialize all modals on the page
     * Flowbite 3.x requires explicit modal initialization (not automatic like earlier versions).
     * This finds all modal elements and creates Modal instances to register them in Flowbite's registry.
     */
    function initializeModals() {
        if (typeof Modal === 'undefined') {
            console.error('Flowbite Modal class not available');
            return;
        }

        document.querySelectorAll('[id$="-modal"]').forEach(function(modalEl) {
            const modal = new Modal(modalEl, {
                backdrop: modalEl.getAttribute('data-modal-backdrop') || 'dynamic',
                closable: true,
            });
            console.log('✓ Initialized modal:', modalEl.id);
        });

        console.log('✓ Modal initialization complete');
    }

    /**
     * Initialize drawers
     * Drawers use Flowbite's automatic initialization via data attributes.
     * No manual instance creation needed (doing so causes conflicting classes).
     */
    function initializeDrawers() {
        console.log('✓ Drawers configured (Flowbite auto-init from data attributes)');
    }

    /**
     * Enforce maximum number of toasts in container
     */
    function enforceMaxToasts() {
        const container = document.getElementById('toast-container');
        if (!container) return;

        const toasts = Array.from(container.querySelectorAll('[role="alert"]'))
            .filter(toast => getComputedStyle(toast).display !== 'none');

        if (toasts.length > TOAST_CONFIG.maxToasts) {
            // Remove oldest toasts (from the end, since we use afterbegin)
            const toastsToRemove = toasts.slice(TOAST_CONFIG.maxToasts);
            toastsToRemove.forEach(function(toast) {
                toast.style.display = 'none';
                console.log('🗑 Removed old toast (max limit):', toast.id);
            });
        }
    }

    /**
     * Initialize toast dismiss functionality
     * Listens for server-triggered initialization via HX-Trigger-After-Settle header.
     * Server passes the exact toast_id to initialize - no DOM scanning needed!
     */
    function initializeToasts() {
        document.body.addEventListener("initialize_toast_dismiss", function(evt) {
            const toastId = evt.detail.toast_id;

            if (!toastId) {
                console.warn('No toast_id provided in initialize_toast_dismiss event');
                return;
            }

            // Find the specific toast by ID (server told us exactly which one)
            const targetEl = document.getElementById(toastId);
            if (!targetEl) {
                console.warn('Toast not found:', toastId);
                return;
            }

            // Find dismiss button in this specific toast
            const dismissTrigger = targetEl.querySelector('[data-dismiss-target]');
            if (!dismissTrigger) {
                console.warn('No dismiss button in toast:', toastId);
                return;
            }

            // Check if already initialized (prevent duplicates)
            if (dismissTrigger.hasAttribute('data-dismiss-initialized')) {
                console.log('Toast already initialized, skipping:', toastId);
                return;
            }

            // Create Dismiss instance for this specific toast
            if (typeof Dismiss !== 'undefined') {
                const dismissInstance = new Dismiss(targetEl, dismissTrigger);
                dismissTrigger.setAttribute('data-dismiss-initialized', 'true');
                console.log('✓ Initialized dismiss via server trigger:', toastId);

                // Auto-dismiss after delay (if enabled)
                if (TOAST_CONFIG.autoDismissDelay > 0) {
                    setTimeout(function() {
                        if (targetEl && getComputedStyle(targetEl).display !== 'none') {
                            dismissInstance.hide();
                            console.log('⏱ Auto-dismissed toast:', toastId);
                        }
                    }, TOAST_CONFIG.autoDismissDelay);
                }
            }

            // Enforce max toasts limit
            enforceMaxToasts();
        });

        console.log('✓ Toast initialization listener registered');
    }

    /**
     * Initialize all Flowbite components on DOMContentLoaded
     */
    function initializeFlowbiteComponents() {
        initializeModals();
        initializeDrawers();
        initializeToasts();
        console.log('✓ flowbite-htmy initialization complete');
    }

    // Run initialization when DOM is ready
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initializeFlowbiteComponents);
    } else {
        // DOM already loaded
        initializeFlowbiteComponents();
    }

    // Expose configuration for user customization
    window.FlowbiteHTMY = {
        config: TOAST_CONFIG,
        reinitialize: initializeFlowbiteComponents
    };
})();
