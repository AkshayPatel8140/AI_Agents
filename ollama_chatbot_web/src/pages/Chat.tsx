import AccountCircle from '@mui/icons-material/AccountCircle'; // User Avatar
import ComputerIcon from '@mui/icons-material/Computer'; // Bot Avatar
import SendIcon from '@mui/icons-material/Send';
import {
  Avatar,
  Box,
  Card,
  FormControl,
  IconButton,
  InputAdornment,
  OutlinedInput,
  Paper,
  Stack,
  Typography,
} from '@mui/material';
import axios from 'axios';
import React from 'react';

const systemPrompt = {
  role: "system",
  content: `
You are Akshay's personal AI assistant. You answer questions about Akshay as if you're his digital representative.

Facts:
- Name: Akshay Patel
- Education: MS in Computer Science at San Francisco Bay University
- Profession: Software Engineer with 4.5+ years of experience in React Native, Node.js, Python, AWS
- Current role: Student Research Assistant at SFBU
- Projects: AI Academic Advisor, SEEKRZ (Buy/Sell App), Jamaica Tours (Uber-style), POS System
- Past companies: eInfochips, Moon Technolabs, Virtual Heights
- Skills: Full Stack Development, AI Integration, RPA, Automation, Amazon FBA Tools
- Based in: USA
- Also runs a UK business called Cloudtail LTD for wholesale
- Interests: Hackathons, AI, Voice UI, and automation
`
};

export const Chat = () => {

  const [input, setInput] = React.useState('');
  const [chat, setChat] = React.useState<{ sender: string; text: string }[]>([]);
  const [loading, setLoading] = React.useState(false);
  const [messageHistory, setMessageHistory] = React.useState([{ role: "system", content: systemPrompt.content }]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMsg = { role: "user", content: input };
    const updatedHistory = [...messageHistory, userMsg];
    setInput('');
    setChat((prev) => [...prev, { sender: 'user', text: input }]);
    setLoading(true);

    try {
      const res = await axios.post('http://localhost:5000/chat', {
        messages: updatedHistory
      });

      const aiReply = res.data.reply;
      const assistantMsg = { role: "assistant", content: aiReply };

      // update chat UI and message memory
      setChat((prev) => [...prev, { sender: 'AI', text: aiReply }]);
      setMessageHistory([...updatedHistory, assistantMsg]);

    } catch (err) {
      console.error("Error:", err);
      setChat((prev) => [...prev, { sender: 'AI', text: "Error from server" }]);
    } finally {
      setLoading(false);
    }
  };


  return (
    <Box sx={{ display: 'flex', flexDirection: 'column', height: '80vh' }} p={4} pt={2}>
      <Box mt={2} flexGrow={1} sx={{ display: 'flex', height: '100%', flexDirection: 'column' }}>
        <Card variant="outlined" sx={{ borderRadius: 2, boxShadow: 10, height: '100%', display: 'flex', flexDirection: 'column', overflow: 'scroll' }}>
          <Box sx={{ px: 2, pt: 1, pr: 2, pb: 1, flexGrow: 1, overflowY: 'auto' }}>
            <Stack spacing={2} sx={{ maxHeight: '100%', scrollBehavior: 'smooth' }}>
              {chat.map((message, index) => (
                <Stack
                  key={index}
                  direction="row"
                  justifyContent={message.sender === 'user' ? 'flex-end' : 'flex-start'}
                  alignItems="flex-start"
                >
                  {message.sender === 'AI' && (
                    <Avatar sx={{ mr: 1 }}>
                      <ComputerIcon />
                    </Avatar>
                  )}
                  <Paper
                    sx={{
                      p: 1.5,
                      borderRadius: '20px',
                      maxWidth: '70%',
                      backgroundColor: message.sender === 'user' ? '#DCF8C6' : '#E1E1E1', // WhatsApp-like colors
                    }}
                  >
                    <Typography variant="body2" style={{ whiteSpace: 'pre-line' }}>
                      {message.text}
                    </Typography>
                  </Paper>
                  {message.sender === 'user' && (
                    <Avatar sx={{ ml: 1 }}>
                      <AccountCircle />
                    </Avatar>
                  )}
                </Stack>
              ))}
              {loading && <p><em>AI is typing...</em></p>}
            </Stack>
          </Box>
          <Box m={3}>
            <FormControl variant="outlined" fullWidth>
              <OutlinedInput
                placeholder="Type a message..."
                value={input}
                onChange={(e) => { setInput(e.target.value) }}
                disabled={loading}
                onKeyDown={(e) => {
                  if (e.key === 'Enter') {
                    e.preventDefault();
                    sendMessage();
                  }
                }}
                endAdornment={
                  <InputAdornment position="end" onClick={sendMessage}>
                    <IconButton>
                      <SendIcon />
                    </IconButton>
                  </InputAdornment>
                }
                inputProps={{ 'aria-label': 'weight' }}
              />
            </FormControl>
          </Box>
        </Card>
      </Box>
    </Box>
  );
};