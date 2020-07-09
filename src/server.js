require("dotenv").config();
import { GraphQLServer } from "graphql-yoga";
import logger from "morgan";
import schema from "./schema";
import { sendSecretMail } from "./utils/utils";

//sendSecretMail("hds2g22@gmail.com", "123");

const PORT = process.env.PORT || 4000;

const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

const server = new GraphQLServer({
  schema,
  context: { prisma },
});
server.express.use(logger("dev"));

server.start({ port: PORT }, () =>
  console.log(`✅ Server running on http://localhost:${PORT}`)
);
