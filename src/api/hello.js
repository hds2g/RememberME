import { isAuthenticated } from "../isAuthenticated";
export default {
  Query: {
    hello: (_, __, { request, prisma }) => {
      isAuthenticated(request);
      return "Hello";
    },
  },
};
