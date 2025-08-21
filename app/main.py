from fastapi import FastAPI
from app.routes import auth_routes, ai_routes, system_routes

app = FastAPI(title="AI Trader API", description="Multi-task AI API for Softvence Omega")

# Register routers
app.include_router(auth_routes.router)
app.include_router(ai_routes.router)
app.include_router(system_routes.router)

if __name__ == "__main__":
    import uvicorn
    from config import OPENROUTER_API_KEY, GROQ_API_KEY, HUGGINGFACE_TOKEN, STABILITY_API_KEY, os

    print("\n" + "="*60)
    print("🚀 AI TRADER API v4.0 STARTING")
    print("="*60)
    print(f"🤖 OpenRouter: {'✅ ENABLED' if OPENROUTER_API_KEY else '❌ DISABLED'}")
    print(f"🤖 Groq: {'✅ ENABLED' if GROQ_API_KEY else '❌ DISABLED'}")
    print(f"🤖 HuggingFace: {'✅ ENABLED' if HUGGINGFACE_TOKEN else '❌ DISABLED'}")
    print(f"🎨 Stability AI: {'✅ ENABLED' if STABILITY_API_KEY else '❌ DISABLED'}")
    print(f"🔐 JWT Auth: ✅ ENABLED")
    print(f"🌐 Port: {os.getenv('PORT', 8000)}")
    print("="*60)
    print("📚 Available Tasks:")
    print("   • qa - Question & Answer")
    print("   • image_generation - Generate Images")
    print("   • content_generation - Social Media Content")
    print("   • latest_answer - Get Last Q&A")
    print("="*60)
    print("🔑 Demo Login: username=demo, password=password")
    print("="*60)

    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
