require("dotenv").config();
import { GraphQLServer } from "graphql-yoga";
import logger from "morgan";
import schema from "./schema";

const PORT = process.env.PORT || 4000;

const server = new GraphQLServer({ schema });
server.express.use(logger("dev"));

const { PrismaClient } = require("@prisma/client");
const prisma = new PrismaClient();

async function main() {
  /*
  await prisma.user.create({
    data: {
      username: "666",
      email: "666.com",
      posts: {
        create: [
          {
            content: "eeee",
            files: {
              create: [{ url: "222.com" }, { url: "333" }],
            },
            categories: {
              connect: [{ id: 5 }, { id: 6 }],
            },
          },
          { content: "fffff" },
        ],
      },
    },
  });
*/

  const allUsers = await prisma.post.findMany();
  console.dir(allUsers, { depth: 2 });
}

main()
  .catch((e) => {
    throw e;
  })
  .finally(async () => {
    await prisma.disconnect();
  });

server.start({ port: PORT }, () =>
  console.log(`✅ Server running on http://localhost:${PORT}`)
);
