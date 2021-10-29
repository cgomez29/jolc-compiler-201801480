import React from "react";
import { Container, Grid, Box, Link } from "@material-ui/core";
import GitHubIcon from "@material-ui/icons/GitHub";

export const Footer = () => {
  return (
    <footer>
      <Box px={{ xs: 3, sm: 10 }} py={{ xs: 5, sm: 10 }} color="white">
        <Container maxWidth="lg">
          <Grid container spacing={5}>
            <Grid item xs={12} sm={6}>
              <Box borderBottom={1} color="black">
                Help
              </Box>
              <Box textAlign="center">
                <Link href="/" color="">
                  user manual
                </Link>
              </Box>
            </Grid>

            <Grid item xs={12} sm={6}>
              <Box borderBottom={1} color="black">
                Repository
              </Box>
              <Box textAlign="center">
                <Link
                  href="https://github.com/cgomez29"
                  target="_blank"
                  color=""
                >
                  <GitHubIcon />
                </Link>
              </Box>
            </Grid>
          </Grid>
          <Box textAlign="center" pt={{ xs: 5, sm: 10 }} pb={{ xs: 5, sm: 0 }}>
            Cristian Gomez &reg;{new Date().getFullYear()}
          </Box>
        </Container>
      </Box>
    </footer>
  );
};
