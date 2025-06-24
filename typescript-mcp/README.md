# MCP TypeScript Client Setup Guide

This guide explains how to set up and run the MCP (Model Context Protocol) TypeScript client with Cursor integration and OpenAI functionality.

## Prerequisites

### Required Tools
- **Node.js**: 18.0 or higher
- **npm**: 9.0 or higher (comes with Node.js)
- **Cursor Editor**: Latest version with MCP support
- **OpenAI API Key**: Required for code review and generation tools

## Setup Instructions

### 1. Install Dependencies

Navigate to the typescript-mcp directory and install all required packages:

```bash
# Install all dependencies
npm install
```

### 2. Set Up Environment Variables

Create a `.env` file in the project root or export the variables:

```bash
# OpenAI API Key (required for AI-powered tools)
export OPENAI_API_KEY="your-openai-api-key-here"
```

### 3. Build the Project

Compile the TypeScript code to JavaScript:

```bash
# Build the project
npm run build
```

### 4. Configure MCP Server in Cursor

#### Step-by-step Cursor Integration:

1. **Open Cursor Settings**:
   - Click on `Cursor` → `Settings` → `Cursor Settings` → `MCP`
   - Click "Add MCP Server"

2. **Add Server Configuration**:
   Use the following JSON configuration:
   ```json
   {
       "mcpServers": {
           "typescript-workshop": {
               "command": "node",
               "args": ["./dist/mcp-server.js"],
               "cwd": "/absolute/path/to/typescript-mcp",
               "env": {
                   "OPENAI_API_KEY": "your-openai-api-key-here"
               }
           }
       }
   }
   ```

3. **Update Configuration Path**:
   - Replace `/absolute/path/to/typescript-mcp` with your actual project path
   - Replace `your-openai-api-key-here` with your actual OpenAI API key

4. **Restart Cursor**:
   Close and reopen Cursor to load the MCP server configuration

### 5. Verify MCP Server Connection

1. **Open Cursor Command Palette**:
   - Press `Cmd/Ctrl + Shift + P`
   - Look for MCP-related commands

2. **Test the Connection**:
   - Use `Cmd/Ctrl + I` to open the AI chat
   - Ask about available MCP tools
   - Verify the server is responding

## Available Tools (Current)

### Code Review Tool
- **Purpose**: Analyzes code files and provides improvement suggestions
- **Parameters**: 
  - `filePath: string` - Absolute path to the code file
- **Usage**: Review TypeScript, JavaScript, Python, and other code files
- **Returns**: Detailed code analysis with suggestions

## Workshop: Adding Code Generation Tool

During the workshop, you'll implement a new code generation tool:

### generate_code
- **Parameters**:
  - `language: string` - Target programming language (typescript, python, java, etc.)
  - `description: string` - Detailed implementation requirements
  - `outputPath: string` - Directory path for generated files
- **Function**: Generates code files based on natural language descriptions
- **Returns**: Array of generated files with code, filenames, and explanations

## Development Commands

```bash
# Install dependencies
npm install

# Build the project
npm run build

# Watch for changes during development
npm run watch

# Type checking
npx tsc --noEmit

# Linting (if configured)
npx eslint src/

# Clean build artifacts
rm -rf dist/
```

## Project Structure

```
typescript-mcp/
├── src/
│   ├── mcp-server.ts          # Main MCP server implementation
│   ├── mcp-client.ts          # MCP client for testing
│   ├── providers/
│   │   └── open-ai.ts         # OpenAI integration
│   └── code-to-review/
│       └── code.ts            # Sample code for testing
├── dist/                      # Compiled JavaScript output
├── package.json               # Dependencies and scripts
├── tsconfig.json             # TypeScript configuration
├── mcp-config.json           # MCP server configuration
└── README.md                 # This file
```

## Usage with Cursor

### Basic Workflow

1. **Start AI Chat**:
   - Open Cursor
   - Press `Cmd/Ctrl + I` to open AI chat
   - Ensure MCP server is connected

2. **Use Code Review**:
   ```
   Please review my code file at /absolute/path/to/your/file.ts
   ```

3. **Generate New Code** (after workshop implementation):
   ```
   Generate a TypeScript React component that displays a user profile card with the following features:
   - Display user avatar, name, and email
   - Show online/offline status
   - Include edit and delete buttons
   ```

## Configuration Files

### mcp-config.json
Contains MCP server metadata and configuration:
```json
{
  "name": "typescript-workshop",
  "version": "1.0.0",
  "description": "TypeScript MCP server for code review and generation",
  "tools": [
    "review-code",
    "generate-code"
  ]
}
```

### tsconfig.json
TypeScript compiler configuration with strict mode and modern target settings.

## Troubleshooting

### Common Issues

**MCP Server Not Found in Cursor**
- Verify the absolute path in `mcp-config.json` is correct
- Ensure the project is built: `npm run build`
- Check that `dist/mcp-server.js` exists
- Restart Cursor after configuration changes

**OpenAI API Errors**
- Verify API key is set: `echo $OPENAI_API_KEY`
- Check API key permissions and usage limits
- Ensure internet connectivity
- Verify API key format (starts with `sk-`)

**TypeScript Compilation Errors**
- Check Node.js version: `node --version` (must be 18+)
- Clear node_modules and reinstall: `rm -rf node_modules && npm install`
- Verify TypeScript version: `npx tsc --version`

**Build Output Missing**
- Run build command: `npm run build`
- Check for compilation errors in console
- Verify `dist/` directory is created

**Code Review Tool Not Working**
- Ensure file paths are absolute, not relative
- Check file permissions and accessibility
- Verify file extensions are supported
- Test with a simple TypeScript file first

### Development Tips

- Use `npm run watch` for auto-compilation during development
- Test tools individually before Cursor integration
- Check Cursor's developer console for MCP-related errors
- Use absolute paths for file operations
- Implement proper error handling in tools

## Advanced Configuration

### Custom Tool Development

1. **Add New Tool Function**:
   ```typescript
   // In mcp-server.ts
   server.setRequestHandler(ListToolsRequestSchema, async () => {
     return {
       tools: [
         // ... existing tools
         {
           name: "your-new-tool",
           description: "Description of your tool",
           inputSchema: {
             type: "object",
             properties: {
               // Define parameters
             }
           }
         }
       ]
     };
   });
   ```

2. **Implement Tool Handler**:
   ```typescript
   server.setRequestHandler(CallToolRequestSchema, async (request) => {
     // Handle your new tool
   });
   ```

3. **Rebuild and Test**:
   ```bash
   npm run build
   # Restart Cursor
   ```

## Resources

- [MCP Documentation](https://modelcontextprotocol.io/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [OpenAI API Documentation](https://platform.openai.com/docs/)
- [Cursor MCP Guide](https://docs.cursor.com/mcp)
- [Node.js Documentation](https://nodejs.org/docs/)

## Contact

For support or contributions, please refer to the workshop materials or contact your instructor.