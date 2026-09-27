"""
Driver Popup UI Component - Enhanced Version with Better Styling
Create this file as: src/driver_popup.py

Displays detailed driver information with photos and beautiful styling
"""

import arcade
import requests
from PIL import Image
from io import BytesIO
from typing import Optional, Dict
import os

class DriverPopup:
    """
    A beautiful popup window showing detailed driver statistics and information
    """
    
    def __init__(self, screen_width: int, screen_height: int):
        self.screen_width = screen_width
        self.screen_height = screen_height
        
        # Popup state
        self.visible = False
        self.driver_info: Optional[Dict] = None
        self.driver_photo = None
        
        # Popup dimensions and position
        self.width = 650
        self.height = 720
        self.x = (screen_width - self.width) // 2
        self.y = (screen_height - self.height) // 2
        
        # Colors - Premium dark theme matching F1 aesthetic
        self.bg_color = (18, 18, 22, 250)  # Deep black-blue
        self.card_bg = (28, 28, 35, 255)   # Slightly lighter
        self.border_color = (70, 70, 80)
        self.text_color = (255, 255, 255)
        self.text_secondary = (160, 165, 175)
        self.accent_color = (229, 47, 65)  # F1 Red
        self.stat_bg = (35, 35, 42, 255)
        self.header_overlay = (0, 0, 0, 120)  # Semi-transparent overlay for header
        
        # Close button
        self.close_button_size = 40
        self.close_button_x = self.x + self.width - self.close_button_size - 12
        self.close_button_y = self.y + self.height - self.close_button_size - 12
        
        # Photo cache directory
        self.cache_dir = os.path.join(os.getcwd(), ".driver_photos")
        if not os.path.exists(self.cache_dir):
            os.makedirs(self.cache_dir)
        
    def show(self, driver_info: Dict):
        """Display the popup with driver information"""
        self.driver_info = driver_info
        self.visible = True
        
        # Load driver photo
        self._load_driver_photo()
        
    def hide(self):
        """Hide the popup"""
        self.visible = False
        self.driver_info = None
        self.driver_photo = None
        
    def _load_driver_photo(self):
        """Download and cache driver photo"""
        if not self.driver_info:
            return
            
        driver_code = self.driver_info.get('driver_code', '')
        photo_url = self.driver_info.get('headshot_url', '')
        
        if not photo_url or not driver_code:
            return
            
        # Check cache first
        cache_path = os.path.join(self.cache_dir, f"{driver_code}.png")
        
        try:
            if os.path.exists(cache_path):
                # Load from cache
                self.driver_photo = arcade.load_texture(cache_path)
            else:
                # Download and cache
                response = requests.get(photo_url, timeout=5)
                response.raise_for_status()
                
                # Save to cache
                img = Image.open(BytesIO(response.content))
                img.save(cache_path)
                
                # Load as texture
                self.driver_photo = arcade.load_texture(cache_path)
        except Exception as e:
            print(f"Could not load driver photo: {e}")
            self.driver_photo = None
        
    def is_close_button_clicked(self, x: float, y: float) -> bool:
        """Check if close button was clicked"""
        if not self.visible:
            return False
            
        return (self.close_button_x <= x <= self.close_button_x + self.close_button_size and
                self.close_button_y <= y <= self.close_button_y + self.close_button_size)
    
    def is_popup_clicked(self, x: float, y: float) -> bool:
        """Check if click is inside popup area"""
        if not self.visible:
            return False
            
        return (self.x <= x <= self.x + self.width and
                self.y <= y <= self.y + self.height)
    
    def draw(self):
        """Draw the popup if visible"""
        if not self.visible or not self.driver_info:
            return
        
        # Draw dark overlay over entire screen
        arcade.draw_lrbt_rectangle_filled(
            0, self.screen_width,
            0, self.screen_height,
            (0, 0, 0, 220)
        )
        
        # Draw main popup background
        self._draw_popup_background()
        
        # Draw header with team color
        self._draw_header()
        
        # Draw driver info section
        self._draw_driver_info()
        
        # Draw stats section
        stats_y = self.y + self.height - 200
        self._draw_stat_cards(stats_y)
        
        # Draw career highlights
        highlights_y = stats_y - 150
        self._draw_career_highlights(highlights_y)
        
        # Draw notable achievements
        achievements_y = highlights_y - 120
        self._draw_achievements(achievements_y)
        
        # Draw close button
        self._draw_close_button()
        
        # Draw instruction text at bottom
        arcade.draw_text(
            "Click anywhere outside to close",
            self.x + self.width // 2,
            self.y + 18,
            self.text_secondary,
            font_size=11,
            anchor_x="center"
        )
    
    def _draw_popup_background(self):
        """Draw popup background with border"""
        # Main background
        arcade.draw_lrbt_rectangle_filled(
            self.x,
            self.x + self.width,
            self.y,
            self.y + self.height,
            self.bg_color
        )
        
        # Outer glow effect (multiple borders)
        for i in range(3):
            alpha = 80 - (i * 25)
            arcade.draw_lrbt_rectangle_outline(
                self.x - i,
                self.x + self.width + i,
                self.y - i,
                self.y + self.height + i,
                (self.accent_color[0], self.accent_color[1], self.accent_color[2], alpha),
                2
            )
        
        # Main border
        arcade.draw_lrbt_rectangle_outline(
            self.x,
            self.x + self.width,
            self.y,
            self.y + self.height,
            self.border_color,
            3
        )
    
    def _draw_header(self):
        """Draw header section with team color gradient"""
        team_color_hex = self.driver_info.get('team_colour', 'E52F41')
        try:
            r, g, b = tuple(int(team_color_hex[i:i+2], 16) for i in (0, 2, 4))
            team_color = (r, g, b)
        except:
            team_color = (229, 47, 65)  # F1 Red fallback
        
        header_height = 160
        
        # Draw team color gradient background
        for i in range(header_height):
            progress = i / header_height
            # Fade from darker to team color
            dark_factor = 0.3 + (progress * 0.5)
            color = tuple(int(team_color[j] * dark_factor) for j in range(3))
            
            arcade.draw_lrbt_rectangle_filled(
                self.x,
                self.x + self.width,
                self.y + self.height - i - 1,
                self.y + self.height - i,
                color + (255,)
            )
        
        # Draw subtle overlay for better text contrast
        arcade.draw_lrbt_rectangle_filled(
            self.x,
            self.x + self.width,
            self.y + self.height - header_height,
            self.y + self.height,
            self.header_overlay
        )
    
    def _draw_driver_info(self):
        """Draw driver name, photo, and basic info"""
        header_start_y = self.y + self.height - 20
        
        # Draw driver photo if available
        photo_x = self.x + 25
        photo_y = self.y + self.height - 140
        
        if self.driver_photo:
            photo_size = 110
            
            # Photo outer glow
            arcade.draw_circle_filled(
                photo_x + photo_size // 2,
                photo_y + photo_size // 2,
                photo_size // 2 + 5,
                (255, 255, 255, 60)
            )
            
            # Photo white border
            arcade.draw_circle_filled(
                photo_x + photo_size // 2,
                photo_y + photo_size // 2,
                photo_size // 2 + 3,
                (255, 255, 255, 255)
            )
            
            # Draw photo
            arcade.draw_texture_rectangle(
                photo_x + photo_size // 2,
                photo_y + photo_size // 2,
                photo_size,
                photo_size,
                self.driver_photo
            )
            
            info_start_x = photo_x + photo_size + 25
        else:
            info_start_x = self.x + 30
        
        # Driver name (large, bold)
        driver_name = self.driver_info.get('full_name', 'Unknown Driver').upper()
        arcade.draw_text(
            driver_name,
            info_start_x,
            header_start_y,
            (255, 255, 255),
            font_size=32,
            bold=True
        )
        
        # Nickname (below name)
        nickname = self.driver_info.get('nickname', '')
        if nickname:
            arcade.draw_text(
                f'"{nickname}"',
                info_start_x,
                header_start_y - 35,
                (230, 230, 240),
                font_size=16,
                italic=True
            )
        
        # Driver number, team, country (one line, well-spaced)
        driver_number = self.driver_info.get('driver_number', 0)
        team_name = self.driver_info.get('team_name', 'Unknown Team')
        country = self.driver_info.get('country_code', '')
        
        info_line = f"#{driver_number}  •  {team_name}  •  {country}"
        
        arcade.draw_text(
            info_line,
            info_start_x,
            header_start_y - 70,
            (200, 205, 215),
            font_size=15,
            bold=True
        )
    
    def _draw_stat_cards(self, y: float):
        """Draw the 4 main stat cards in a grid"""
        card_width = 145
        card_height = 95
        gap = 20
        start_x = self.x + 25
        
        stats = [
            ("CHAMPIONSHIPS", self.driver_info.get('championships', 0)),
            ("RACE WINS", self.driver_info.get('career_wins', 0)),
            ("POLE POSITIONS", self.driver_info.get('pole_positions', 0)),
            ("PODIUMS", self.driver_info.get('podiums', 0)),
        ]
        
        for i, (label, value) in enumerate(stats):
            row = i // 2
            col = i % 2
            
            card_x = start_x + col * (card_width + gap)
            card_y = y - row * (card_height + gap)
            
            # Card background with subtle gradient
            arcade.draw_lrbt_rectangle_filled(
                card_x,
                card_x + card_width,
                card_y - card_height,
                card_y,
                self.stat_bg
            )
            
            # Card border
            arcade.draw_lrbt_rectangle_outline(
                card_x,
                card_x + card_width,
                card_y - card_height,
                card_y,
                (self.accent_color[0], self.accent_color[1], self.accent_color[2], 100),
                2
            )
            
            # Draw value (large, centered)
            arcade.draw_text(
                str(value),
                card_x + card_width // 2,
                card_y - 40,
                self.accent_color,
                font_size=42,
                bold=True,
                anchor_x="center"
            )
            
            # Draw label (centered below value)
            arcade.draw_text(
                label,
                card_x + card_width // 2,
                card_y - 75,
                self.text_secondary,
                font_size=12,
                bold=True,
                anchor_x="center"
            )
    
    def _draw_career_highlights(self, y: float):
        """Draw additional career information"""
        section_x = self.x + 350
        
        # Section title
        arcade.draw_text(
            "CAREER HIGHLIGHTS",
            section_x,
            y + 60,
            self.accent_color,
            font_size=15,
            bold=True
        )
        
        # Divider line
        arcade.draw_line(
            section_x,
            y + 50,
            section_x + 250,
            y + 50,
            self.accent_color,
            2
        )
        
        # Career details
        details = [
            ("Best Finish", "1st" if self.driver_info.get('career_wins', 0) > 0 else "TBD"),
            ("Fastest Laps", "TBD"),
            ("Championships", str(self.driver_info.get('championships', 0))),
            ("Current Team", self.driver_info.get('team_name', 'N/A')),
        ]
        
        current_y = y + 25
        for label, value in details:
            # Label (left aligned)
            arcade.draw_text(
                label,
                section_x,
                current_y,
                self.text_secondary,
                font_size=13
            )
            
            # Value (right aligned)
            arcade.draw_text(
                str(value),
                section_x + 250,
                current_y,
                self.text_color,
                font_size=13,
                bold=True,
                anchor_x="right"
            )
            current_y -= 26
    
    def _draw_achievements(self, y: float):
        """Draw notable achievements section"""
        achievements = self.driver_info.get('notable_achievements', [])
        if not achievements:
            return
        
        # Section title
        arcade.draw_text(
            "NOTABLE ACHIEVEMENTS",
            self.x + 25,
            y,
            self.accent_color,
            font_size=15,
            bold=True
        )
        
        # Divider line
        arcade.draw_line(
            self.x + 25,
            y - 10,
            self.x + self.width - 25,
            y - 10,
            self.accent_color,
            2
        )
        
        current_y = y - 30
        
        for achievement in achievements[:5]:  # Show max 5
            # Bullet point
            arcade.draw_circle_filled(
                self.x + 35,
                current_y + 5,
                3,
                self.accent_color
            )
            
            # Achievement text with word wrap
            if len(achievement) > 70:
                words = achievement.split()
                lines = []
                current_line = []
                current_length = 0
                
                for word in words:
                    if current_length + len(word) + 1 <= 70:
                        current_line.append(word)
                        current_length += len(word) + 1
                    else:
                        lines.append(' '.join(current_line))
                        current_line = [word]
                        current_length = len(word)
                
                if current_line:
                    lines.append(' '.join(current_line))
                
                for line in lines:
                    arcade.draw_text(
                        line,
                        self.x + 45,
                        current_y,
                        self.text_color,
                        font_size=12
                    )
                    current_y -= 20
            else:
                arcade.draw_text(
                    achievement,
                    self.x + 45,
                    current_y,
                    self.text_color,
                    font_size=12
                )
                current_y -= 22
    
    def _draw_close_button(self):
        """Draw the close (X) button with premium styling"""
        center_x = self.close_button_x + self.close_button_size // 2
        center_y = self.close_button_y + self.close_button_size // 2
        
        # Outer glow
        arcade.draw_circle_filled(
            center_x, center_y,
            self.close_button_size // 2 + 3,
            (self.accent_color[0], self.accent_color[1], self.accent_color[2], 80)
        )
        
        # Button background
        arcade.draw_circle_filled(
            center_x, center_y,
            self.close_button_size // 2,
            self.accent_color
        )
        
        # X symbol (thicker, better positioned)
        offset = 10
        
        arcade.draw_line(
            center_x - offset, center_y - offset,
            center_x + offset, center_y + offset,
            (255, 255, 255), 4
        )
        arcade.draw_line(
            center_x - offset, center_y + offset,
            center_x + offset, center_y - offset,
            (255, 255, 255), 4
        )

# Example usage for testing
if __name__ == "__main__":
    print("Enhanced DriverPopup class with improved styling!")
    print("Features: Better colors, alignment, and premium F1 aesthetic!")