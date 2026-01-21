/**
 * CRUD Tank - Fish Swimming Animation
 *
 * This script handles the swimming animation for fish in the tank.
 * Each fish moves around randomly based on their personality (speed).
 */

document.addEventListener('DOMContentLoaded', function() {
    // Get all fish elements
    const fishElements = document.querySelectorAll('.fish');

    // Tank boundaries (we need to keep fish inside the tank)
    const tank = document.querySelector('.tank');
    if (!tank) return; // Exit if we're not on the tank page

    // Animation speeds based on personality
    const speeds = {
        slow: { min: 0.3, max: 0.6 },
        medium: { min: 0.6, max: 1.2 },
        fast: { min: 1.2, max: 2.0 }
    };

    // Initialize each fish with its own animation
    fishElements.forEach(fish => {
        initFishAnimation(fish);
    });

    /**
     * Initialize swimming animation for a single fish
     */
    function initFishAnimation(fish) {
        const personality = fish.dataset.personality || 'medium';
        const speedRange = speeds[personality] || speeds.medium;

        // Fish state
        let state = {
            x: parseFloat(fish.style.left) || Math.random() * 70 + 5,
            y: parseFloat(fish.style.top) || Math.random() * 50 + 10,
            vx: (Math.random() - 0.5) * 2,
            vy: (Math.random() - 0.5) * 2,
            speed: speedRange.min + Math.random() * (speedRange.max - speedRange.min),
            targetX: null,
            targetY: null,
            direction: 1, // 1 = right, -1 = left
            wobble: 0
        };

        // Set initial position
        fish.style.left = state.x + '%';
        fish.style.top = state.y + '%';

        // Pick a new random target
        pickNewTarget(state);

        // Start animation loop
        animateFish(fish, state, speedRange);
    }

    /**
     * Pick a new random target position for the fish
     */
    function pickNewTarget(state) {
        state.targetX = Math.random() * 75 + 5; // 5% to 80% of tank width
        state.targetY = Math.random() * 55 + 10; // 10% to 65% of tank height
    }

    /**
     * Main animation loop for a single fish
     */
    function animateFish(fish, state, speedRange) {
        const fishImage = fish.querySelector('.fish-image');

        function update() {
            // Calculate direction to target
            const dx = state.targetX - state.x;
            const dy = state.targetY - state.y;
            const distance = Math.sqrt(dx * dx + dy * dy);

            // If we're close to target, pick a new one
            if (distance < 3) {
                pickNewTarget(state);
                // Slightly randomize speed when changing direction
                state.speed = speedRange.min + Math.random() * (speedRange.max - speedRange.min);
            }

            // Move towards target
            const moveX = (dx / distance) * state.speed * 0.5;
            const moveY = (dy / distance) * state.speed * 0.3;

            state.x += moveX;
            state.y += moveY;

            // Add subtle wobble for more natural movement
            state.wobble += 0.1;
            const wobbleOffset = Math.sin(state.wobble) * 0.3;

            // Clamp position to tank boundaries
            state.x = Math.max(2, Math.min(88, state.x));
            state.y = Math.max(5, Math.min(70, state.y));

            // Update fish direction (flip image when changing direction)
            const newDirection = moveX > 0 ? 1 : -1;
            if (newDirection !== state.direction) {
                state.direction = newDirection;
            }

            // Apply position and rotation
            fish.style.left = state.x + '%';
            fish.style.top = (state.y + wobbleOffset) + '%';

            // Flip fish image based on direction and add slight tilt
            const tilt = moveY * 5; // Tilt based on vertical movement
            if (fishImage) {
                fishImage.style.transform = `scaleX(${state.direction}) rotate(${tilt}deg)`;
            }

            // Continue animation
            requestAnimationFrame(update);
        }

        // Start the animation loop
        update();
    }

    /**
     * Add hover pause effect
     * Fish pauses briefly when you hover over it
     */
    fishElements.forEach(fish => {
        fish.addEventListener('mouseenter', () => {
            fish.style.animationPlayState = 'paused';
        });

        fish.addEventListener('mouseleave', () => {
            fish.style.animationPlayState = 'running';
        });
    });

    /**
     * Add random bubble generation
     */
    const bubblesContainer = document.querySelector('.bubbles');
    if (bubblesContainer) {
        setInterval(() => {
            if (Math.random() > 0.7) { // 30% chance every interval
                createBubble(bubblesContainer);
            }
        }, 2000);
    }

    function createBubble(container) {
        const bubble = document.createElement('div');
        bubble.className = 'bubble';
        bubble.style.left = (Math.random() * 90 + 5) + '%';
        bubble.style.width = (Math.random() * 8 + 4) + 'px';
        bubble.style.height = bubble.style.width;
        bubble.style.animationDuration = (Math.random() * 3 + 3) + 's';

        container.appendChild(bubble);

        // Remove bubble after animation completes
        setTimeout(() => {
            bubble.remove();
        }, 6000);
    }
});

/**
 * Utility: Add some visual feedback when clicking on fish
 */
document.addEventListener('click', function(e) {
    const fishLink = e.target.closest('.fish-link');
    if (fishLink) {
        const fish = fishLink.closest('.fish');
        if (fish) {
            fish.style.transform = 'scale(1.2)';
            setTimeout(() => {
                fish.style.transform = '';
            }, 200);
        }
    }
});
