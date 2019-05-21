using System;
using System.Collections.Generic;
using System.Linq;
using Microsoft.Xna.Framework;
using Microsoft.Xna.Framework.Audio;
using Microsoft.Xna.Framework.Content;
using Microsoft.Xna.Framework.GamerServices;
using Microsoft.Xna.Framework.Graphics;
using Microsoft.Xna.Framework.Input;
using Microsoft.Xna.Framework.Media;

namespace step8
{
    /// <summary>
    /// This is the main type for your game
    /// </summary>
    public class Game1 : Microsoft.Xna.Framework.Game
    {
        GraphicsDeviceManager graphics;
        SpriteBatch spriteBatch;
        Texture2D texture1;
        Texture2D texture2;
        Texture2D texture3;

        Vector2 spritePosition1;
        Vector2 spritePosition2;
        Vector2 spritePosition3;
        Vector2 spriteSpeed1 = new Vector2(50.0f, 50.0f);
        Vector2 spriteSpeed2 = new Vector2(100.0f, 100.0f);
        Vector2 spriteSpeed3 = new Vector2(0.0f, 0.0f);

        int sprite1Height;
        int sprite1Width;
        int sprite2Height;
        int sprite2Width;
        int sprite3Height;
        int sprite3Width;

        float angle = 0;

        SoundEffect soundEffect;

        public Game1()
        {
            graphics = new GraphicsDeviceManager(this);
            Content.RootDirectory = "Content";
        }

        /// <summary>
        /// Allows the game to perform any initialization it needs to before starting to run.
        /// This is where it can query for any required services and load any non-graphic
        /// related content.  Calling base.Initialize will enumerate through any components
        /// and initialize them as well.
        /// </summary>
        protected override void Initialize()
        {
            // TODO: Add your initialization logic here

            base.Initialize();
        }

        /// <summary>
        /// LoadContent will be called once per game and is the place to load
        /// all of your content.
        /// </summary>
        protected override void LoadContent()
        {
            // Create a new SpriteBatch, which can be used to draw textures

            spriteBatch = new SpriteBatch(GraphicsDevice);

            texture1 = Content.Load<Texture2D>("ball");
            texture2 = Content.Load<Texture2D>("google");
            texture3 = Content.Load<Texture2D>("apple");

            soundEffect = Content.Load<SoundEffect>("chimes");

            spritePosition1.X = 0;
            spritePosition1.Y = 0;

            spritePosition2.X = graphics.GraphicsDevice.Viewport.Width - texture1.Width;
            spritePosition2.Y = graphics.GraphicsDevice.Viewport.Height - texture1.Height;

            spritePosition3.X = graphics.GraphicsDevice.Viewport.Width/2;
            spritePosition3.Y = 0;

            sprite1Height = texture1.Bounds.Height;
            sprite1Width = texture1.Bounds.Width;

            sprite2Height = texture2.Bounds.Height;
            sprite2Width = texture2.Bounds.Width;

            sprite3Height = texture3.Bounds.Height;
            sprite3Width = texture3.Bounds.Width;


        }

        /// <summary>
        /// UnloadContent will be called once per game and is the place to unload
        /// all content.
        /// </summary>
        protected override void UnloadContent()
        {
            // TODO: Unload any non ContentManager content here
        }

        /// <summary>
        /// Allows the game to run logic such as updating the world,
        /// checking for collisions, gathering input, and playing audio.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Update(GameTime gameTime)
        {
            // Allow the game to exit

            if (GamePad.GetState(PlayerIndex.One).Buttons.Back == ButtonState.Pressed)
                this.Exit();

            // Move the sprite around
            angle += 0.01f;


            UpdateSprite(gameTime, ref spritePosition1, ref spriteSpeed1);
            UpdateSprite(gameTime, ref spritePosition2, ref spriteSpeed2);
            UpdateSprite(gameTime, ref spritePosition3, ref spriteSpeed3);
            CheckForCollision();

            base.Update(gameTime);
        }

        /// <summary>
        /// This is called when the game should draw itself.
        /// </summary>
        /// <param name="gameTime">Provides a snapshot of timing values.</param>
        protected override void Draw(GameTime gameTime)
        {
            graphics.GraphicsDevice.Clear(Color.CornflowerBlue);

            // Draw the sprite

            spriteBatch.Begin(SpriteSortMode.BackToFront, BlendState.AlphaBlend);
            spriteBatch.Draw(texture1, spritePosition1, Color.White);
            spriteBatch.End();

            spriteBatch.Begin(SpriteSortMode.BackToFront, BlendState.Opaque);
            spriteBatch.Draw(texture2, spritePosition2, Color.White);
            spriteBatch.End();

            spriteBatch.Begin(SpriteSortMode.BackToFront, BlendState.Opaque);
            Rectangle sourceRectangle = new Rectangle(0, 0, texture3.Width, texture3.Height);
            Vector2 origin = new Vector2(0, 0);
            spriteBatch.Draw(texture3, spritePosition3, sourceRectangle, Color.White, angle, origin, 1.0f, SpriteEffects.None, 1);
            spriteBatch.End();

            base.Draw(gameTime);
        }

        void UpdateSprite(GameTime gameTime, ref Vector2 spritePosition, ref Vector2 spriteSpeed)
        {

            // Move the sprite by speed, scaled by elapsed time 

            angle += 0.01f;

            spritePosition += spriteSpeed * (float)gameTime.ElapsedGameTime.TotalSeconds;

            int MaxX = graphics.GraphicsDevice.Viewport.Width - texture1.Width;
            int MinX = 0;
            int MaxY = graphics.GraphicsDevice.Viewport.Height - texture1.Height;
            int MinY = 0;

            // Check for bounce 

            if (spritePosition.X > MaxX)
            {

                spriteSpeed.X *= -1;
                spritePosition.X = MaxX;
            }

            else if (spritePosition.X < MinX)
            {

                spriteSpeed.X *= -1;
                spritePosition.X = MinX;
            }

            if (spritePosition.Y > MaxY)
            {

                spriteSpeed.Y *= -1;
                spritePosition.Y = MaxY;
            }

            else if (spritePosition.Y < MinY)
            {

                spriteSpeed.Y *= -1;
                spritePosition.Y = MinY;
            }
        }

        void CheckForCollision()
        {

            BoundingBox bb1 = new BoundingBox(new Vector3(spritePosition1.X - (sprite1Width / 2), spritePosition1.Y - (sprite1Height / 2), 0), new Vector3(spritePosition1.X + (sprite1Width / 2), spritePosition1.Y + (sprite1Height / 2), 0));

            BoundingBox bb2 = new BoundingBox(new Vector3(spritePosition2.X - (sprite2Width / 2), spritePosition2.Y - (sprite2Height / 2), 0), new Vector3(spritePosition2.X + (sprite2Width / 2), spritePosition2.Y + (sprite2Height / 2), 0));

            if (bb1.Intersects(bb2))
            {
                spriteSpeed1.X *= -1;
                spriteSpeed1.Y *= -1;
                spriteSpeed2.X *= -1;
                spriteSpeed2.Y *= -1;

                soundEffect.Play();

            }
        }
    }
}
