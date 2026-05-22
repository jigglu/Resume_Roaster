import typer
from pathlib import Path
from langchain_community.document_loaders import PyPDFLoader
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate

app = typer.Typer(help="Resume Roaster CLI")

@app.command()
def roast(file_path: str):
    """Feed your resume to a ruthless AI recruiter."""
    path = Path(file_path)

    if not path.exists():
        typer.echo(f"❌ Error: File '{file_path}' not found. Did you even try?")
        raise typer.Exit(code=1)

    if path.suffix != ".pdf":
        typer.echo("❌ Error: I only roast .pdf files. Convert it and come back.")
        raise typer.Exit(code=1)

    typer.echo(f"📄 Scanning '{file_path}' (prepare to cry)...")
    loader = PyPDFLoader(str(path))
    docs = loader.load()
    resume_text = "\n".join([doc.page_content for doc in docs])

    if not resume_text.strip():
        typer.echo("❌ This PDF has no readable text. Automatic rejection.")
        raise typer.Exit(code=1)

    typer.echo("🔥 Heating up the roaster...")
    llm = ChatGroq(model="llama3-8b-8192", api_key="your_groq_key_here")
    prompt = PromptTemplate.from_template(
        "You are the most ruthless, cynical, and brutally honest tech recruiter on Earth. "
        "You have zero patience for fluff, buzzwords, and vague accomplishments. "
        "Tear this resume apart. Highlight weak action verbs, vague bullet points, "
        "lack of hard metrics, and anything trash-worthy. "
        "Be sarcastic and brutal but technically valid.\n\n"
        "Resume:\n<resume>\n{resume_text}\n</resume>\n\nRoast:"
    )
    chain = prompt | llm
    response = chain.invoke({"resume_text": resume_text})
    typer.echo("\n💀 THE ROAST:\n")
    typer.echo(response)

if __name__ == "__main__":
    app()
