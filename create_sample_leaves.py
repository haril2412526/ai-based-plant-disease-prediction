"""
Generate sample plant leaf images for instant 1-click testing in PlantCare AI.
"""

import os
import cv2
import numpy as np

OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "static", "images", "samples")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def create_leaf_canvas(w=500, h=500, bg_color=(242, 245, 243)):
    """Create a soft neutral backdrop for leaf specimen."""
    canvas = np.full((h, w, 3), bg_color, dtype=np.uint8)
    # Add subtle background texture
    noise = np.random.randint(-5, 5, (h, w, 3), dtype=np.int16)
    canvas = np.clip(canvas.astype(np.int16) + noise, 0, 255).astype(np.uint8)
    return canvas

def draw_leaf_base(canvas, center=(250, 250), size=(130, 200), angle=0, base_color=(45, 135, 50)):
    """Draw realistic elliptical compound leaf structure with primary veins."""
    mask = np.zeros(canvas.shape[:2], dtype=np.uint8)
    cv2.ellipse(mask, center, size, angle, 0, 360, 255, -1)
    
    # Slight leaf tip distortion
    tip = (int(center[0]), int(center[1] - size[1] * 0.95))
    cv2.circle(mask, tip, int(size[0]*0.3), 255, -1)

    # Colorize leaf blade
    leaf_layer = np.full_like(canvas, base_color)
    # Add subtle gradient/shading
    for y in range(canvas.shape[0]):
        factor = 1.0 - 0.2 * abs(y - center[1]) / (size[1] + 1)
        leaf_layer[y, :] = np.clip(leaf_layer[y, :] * factor, 0, 255).astype(np.uint8)

    # Apply to canvas
    leaf_idx = mask == 255
    canvas[leaf_idx] = leaf_layer[leaf_idx]

    # Draw Central Midrib & Secondary Lateral Veins
    vein_color = (int(base_color[0]*1.15), int(base_color[1]*1.25), int(base_color[2]*1.15))
    start_stem = (center[0], center[1] + size[1] + 40)
    end_tip = (center[0], center[1] - size[1] + 10)
    cv2.line(canvas, start_stem, end_tip, vein_color, 4, cv2.LINE_AA)

    # Lateral veins
    for i in range(-4, 5):
        y_pos = int(center[1] + i * (size[1] // 5.5))
        if y_pos > end_tip[1] + 20 and y_pos < start_stem[1] - 40:
            cv2.line(canvas, (center[0], y_pos), (center[0] - int(size[0]*0.75), y_pos - 30), vein_color, 2, cv2.LINE_AA)
            cv2.line(canvas, (center[0], y_pos), (center[0] + int(size[0]*0.75), y_pos - 30), vein_color, 2, cv2.LINE_AA)

    return mask

def generate_healthy_tomato():
    canvas = create_leaf_canvas()
    draw_leaf_base(canvas, base_color=(35, 145, 55))
    path = os.path.join(OUTPUT_DIR, "tomato_healthy_sample.jpg")
    cv2.imwrite(path, canvas)
    print("Saved:", path)

def generate_early_blight_tomato():
    canvas = create_leaf_canvas()
    mask = draw_leaf_base(canvas, base_color=(45, 130, 45))
    
    # Target concentric spots with yellow halos
    spots = [(210, 200, 26), (290, 270, 34), (230, 310, 22), (280, 180, 20), (190, 260, 18)]
    for (sx, sy, r) in spots:
        # Outer yellow halo
        cv2.circle(canvas, (sx, sy), int(r * 1.6), (60, 200, 210), -1) # BGR: yellow/chlorotic
        # Brown necrotic ring
        cv2.circle(canvas, (sx, sy), r, (25, 50, 100), -1)
        # Inner bullseye rings
        cv2.circle(canvas, (sx, sy), int(r * 0.65), (20, 38, 75), 2)
        cv2.circle(canvas, (sx, sy), int(r * 0.35), (15, 25, 50), -1)

    path = os.path.join(OUTPUT_DIR, "tomato_early_blight_sample.jpg")
    cv2.imwrite(path, canvas)
    print("Saved:", path)

def generate_late_blight_tomato():
    canvas = create_leaf_canvas()
    mask = draw_leaf_base(canvas, base_color=(40, 120, 40))

    # Large water-soaked brownish-black irregular lesions
    lesion_centers = [(230, 190), (280, 250), (200, 300)]
    for lx, ly in lesion_centers:
        cv2.ellipse(canvas, (lx, ly), (65, 45), 35, 0, 360, (20, 35, 45), -1)
        # Add fuzzy grayish margin
        cv2.ellipse(canvas, (lx, ly), (75, 52), 35, 0, 360, (110, 130, 120), 3)

    path = os.path.join(OUTPUT_DIR, "tomato_late_blight_sample.jpg")
    cv2.imwrite(path, canvas)
    print("Saved:", path)

def generate_potato_early_blight():
    canvas = create_leaf_canvas()
    draw_leaf_base(canvas, size=(145, 190), base_color=(50, 138, 48))
    # Target spots
    spots = [(220, 220, 30), (275, 290, 25), (210, 320, 20)]
    for (sx, sy, r) in spots:
        cv2.circle(canvas, (sx, sy), int(r * 1.5), (55, 195, 205), -1)
        cv2.circle(canvas, (sx, sy), r, (30, 60, 110), -1)
        cv2.circle(canvas, (sx, sy), int(r * 0.5), (15, 30, 65), -1)

    path = os.path.join(OUTPUT_DIR, "potato_early_blight_sample.jpg")
    cv2.imwrite(path, canvas)
    print("Saved:", path)

def generate_apple_scab():
    canvas = create_leaf_canvas()
    draw_leaf_base(canvas, size=(125, 190), base_color=(55, 125, 45))
    # Corky olive green to velvety black scabs
    scabs = [(220, 180, 22), (280, 220, 28), (240, 290, 30), (260, 340, 18)]
    for (sx, sy, r) in scabs:
        cv2.circle(canvas, (sx, sy), r, (28, 55, 55), -1) # olive dark
        cv2.circle(canvas, (sx, sy), int(r*0.7), (18, 30, 35), -1) # blackish crust

    path = os.path.join(OUTPUT_DIR, "apple_scab_sample.jpg")
    cv2.imwrite(path, canvas)
    print("Saved:", path)

if __name__ == "__main__":
    generate_healthy_tomato()
    generate_early_blight_tomato()
    generate_late_blight_tomato()
    generate_potato_early_blight()
    generate_apple_scab()
    print("All sample leaf specimens created successfully!")
