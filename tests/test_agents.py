"""
Simple tests for the AI Agent Application.
"""
import pytest
from src.agents.sample_agent import SampleAgent


@pytest.mark.asyncio
async def test_sample_agent_initialization():
    """Test that SampleAgent initializes correctly."""
    agent = SampleAgent()
    assert agent.name == "sample-agent"
    assert agent.model is not None
    assert agent.temperature >= 0
    assert agent.max_iterations > 0


@pytest.mark.asyncio
async def test_sample_agent_execute():
    """Test that SampleAgent executes tasks."""
    agent = SampleAgent()
    result = await agent.execute("test task")
    
    assert result is not None
    assert result["status"] == "success"
    assert "task" in result
    assert result["task"] == "test task"
    assert "response" in result


@pytest.mark.asyncio
async def test_sample_agent_execute_with_context():
    """Test that SampleAgent handles context."""
    agent = SampleAgent()
    context = {"source": "test", "user_id": "123"}
    result = await agent.execute("test task with context", context)
    
    assert result["status"] == "success"
    assert result["context_provided"] is True
    assert "context_keys" in result


@pytest.mark.asyncio
async def test_sample_agent_analyze():
    """Test the analyze method."""
    agent = SampleAgent()
    result = await agent.analyze("test data")
    
    assert result is not None
    assert result["status"] == "success"


@pytest.mark.asyncio
async def test_sample_agent_generate():
    """Test the generate method."""
    agent = SampleAgent()
    result = await agent.generate("test prompt")
    
    assert result is not None
    assert result["status"] == "success"


@pytest.mark.asyncio
async def test_execution_history():
    """Test that execution history is tracked."""
    agent = SampleAgent()
    await agent.execute("task 1")
    await agent.execute("task 2")
    
    history = agent.get_execution_history()
    assert len(history) == 2
    assert history[0]["task"] == "task 1"
    assert history[1]["task"] == "task 2"


@pytest.mark.asyncio
async def test_clear_history():
    """Test that execution history can be cleared."""
    agent = SampleAgent()
    await agent.execute("task 1")
    
    assert len(agent.get_execution_history()) == 1
    
    agent.clear_history()
    assert len(agent.get_execution_history()) == 0
