import Box from '@mui/material/Box';
import Button from '@mui/material/Button';
import MuiCard from '@mui/material/Card';
import CssBaseline from '@mui/material/CssBaseline';
import Stack from '@mui/material/Stack';
import { styled } from '@mui/material/styles';
import { useNavigate } from 'react-router-dom';
import { Colors } from '../components/Colors.tsx';

const Card = styled(MuiCard)(({ theme }) => ({
    display: 'flex',
    flexDirection: 'column',
    alignSelf: 'center',
    width: '100%',
    padding: theme.spacing(4),
    gap: theme.spacing(2),
    margin: 'auto',
    [theme.breakpoints.up('sm')]: { maxWidth: '450px' },
    boxShadow: 'hsla(220, 30%, 5%, 0.05) 0px 5px 15px 0px, hsla(220, 25%, 10%, 0.05) 0px 15px 35px -5px',
    ...theme.applyStyles('dark', {
        boxShadow: 'hsla(220, 30%, 5%, 0.5) 0px 5px 15px 0px, hsla(220, 25%, 10%, 0.08) 0px 15px 35px -5px',
    }),
}));

const Container = styled(Stack)(({ theme }) => ({
    height: 'calc((1 - var(--template-frame-height, 0)) * 100dvh)',
    minHeight: '100%',
    padding: theme.spacing(2),
    [theme.breakpoints.up('sm')]: { padding: theme.spacing(4) },
    '&::before': {
        content: '""',
        display: 'block',
        position: 'absolute',
        zIndex: -1,
        inset: 0,
        backgroundImage: 'radial-gradient(ellipse at 50% 50%, hsl(210, 100%, 97%), hsl(0, 0%, 100%))',
        backgroundRepeat: 'no-repeat',
        ...theme.applyStyles('dark', {
            backgroundImage: 'radial-gradient(at 50% 50%, hsla(210, 100%, 16%, 0.5), hsl(220, 30%, 5%))',
        }),
    },
}));

export function Dashboard(props: { disableCustomTheme?: boolean }) {

    const navigate = useNavigate()
    const handleSubmit = () => { navigate('/chat'); };

    return (
        <>
            <CssBaseline enableColorScheme />
            <Container direction="column" justifyContent="space-between">

                <Card variant="outlined">
                    <Box
                        sx={{
                            display: 'flex',
                            flexDirection: 'column',
                            width: '100%',
                            gap: 2
                        }}
                    >
                        <Button
                            fullWidth
                            variant="contained"
                            size="large"
                            sx={{ backgroundColor: Colors.defaultBlue }}
                            onClick={handleSubmit}
                        >
                            Open Chat
                        </Button>
                    </Box>
                </Card>
            </Container>
        </>
    );
}