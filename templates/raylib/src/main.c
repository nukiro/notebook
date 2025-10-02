#include "raylib.h"

int main(void)
{
    const int screenWidth = 800;
    const int screenHeight = 450;

    InitWindow(screenWidth, screenHeight, "Basic Window");

    SetTargetFPS(60);
    while (!WindowShouldClose())
    {
        BeginDrawing();
        ClearBackground(BLACK);
        DrawText("Congrats! You created your first window!", 190, 200, 20, RAYWHITE);
        EndDrawing();
    }
    CloseWindow();

    return 0;
}